from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

def get_ai_response(user_input):
    """Generate AI response using GPT API"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    ai_reply = get_ai_response(user_message)
    return jsonify({"response": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
