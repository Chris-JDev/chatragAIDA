from flask import Flask, render_template, request, jsonify
from aida_classifier import classify_aida_stage
import subprocess

app = Flask(__name__)

# Utility to call Ollama model server (assumes ollama is running locally)
def query_ollama(prompt: str) -> str:
    result = subprocess.run([
        'ollama', 'serve', 'chatgpt4o-mini', '--prompt', prompt
    ], capture_output=True, text=True)
    return result.stdout.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    # Query the LLM via Ollama
    bot_response = query_ollama(user_input)
    # Classify AIDA
    stage = classify_aida_stage(bot_response)
    return jsonify({
        'response': bot_response,
        'aida_stage': stage
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
