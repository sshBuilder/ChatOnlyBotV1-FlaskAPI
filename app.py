from flask import Flask, request, jsonify, render_template
import requests
import json
from markdown import markdown  # Add this import

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3.2",
        "prompt": user_message,
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        return jsonify({"error": "Failed to get response from Ollama API"}), 500

    response_data = response.json()
    response_text = response_data.get('response', '')
    response_html = markdown(response_text)  # Convert Markdown to HTML
    return jsonify({"response": response_html})

if __name__ == '__main__':
    app.run(debug=True)
