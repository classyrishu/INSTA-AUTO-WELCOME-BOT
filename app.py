from flask import Flask, request, jsonify
import os

app = Flask(__name__)

WELCOME_MSG = "Welcome to the GC! Rules follow karo, enjoy karo. Introduce yourself - Naam / City?"

@app.route('/')
def home():
    return "IG GC Welcome Bot is Running!"

@app.route('/welcome', methods=['POST'])
def welcome():
    data = request.json
    username = data.get('username', 'New Member')
    print(f"New member joined: {username}")
    return jsonify({"message": f"Hi {username}, {WELCOME_MSG}"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
