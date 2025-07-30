from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Your OpenRouter API key here (keep it secret!)
OPENROUTER_API_KEY = "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"  # paste your real key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']

        # Prepare headers and data for OpenRouter
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",  # you can change to other models like mistralai/mixtral-8x7b if you want
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
            return jsonify({"reply": reply})
        else:
            return jsonify({"error": f"Error: {response.status_code} - {response.text}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
