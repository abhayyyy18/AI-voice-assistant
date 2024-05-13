from flask import Flask, render_template, jsonify
from main import main , listen  # Import the main function from your voice assistant logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_voice_input', methods=['POST'])
def get_voice_input():
    # Capture voice input
    user_input = listen()

    # Process user input using the main function
    main()  # Call the main function without passing any arguments

    # Return a response (if needed)
    return jsonify({'response': 'Voice command executed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
