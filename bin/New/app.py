from flask import Flask, request, jsonify
from flask_cors import CORS
from base64 import b64decode as b64d
from base64 import b64encode as b64e
#
#
app = Flask(__name__)
CORS(app)

@app.route('/api/', methods=['POST'])
def call_api():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No data received"}), 400
    txt = data['data']
    print(txt)
    resulting = ML(txt)
    resulting.header("Access-Control-Allow-Origin", "*")
    resulting.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")


def ML(user_input):
    MAX_ITERATIONS = 5
    
    history = [
        {"role": "system", "content": "You are an intelligent teaching assistant. You always provide well-reasoned answers that are both correct and helpful."},
        {"role": "user", "content": user_input},
    ]

    for _ in range(MAX_ITERATIONS):
        completion = client.chat.completions.create(
            model="local-model", # this field is currently unused
            messages=history,
            temperature=0.7,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}
        
        for chunk in completion:
            if chunk.choices[0].delta.content:
                new_message["content"] += chunk.choices[0].delta.content

                # Check if the assistant's response is complete
                if "Thank you, that's all." in chunk.choices[0].delta.content:
                    return new_message["content"]

        history.append(new_message)
        history.append({"role": "user", "content": input("> ")})
        
if __name__ == '__main__':
    app.run()