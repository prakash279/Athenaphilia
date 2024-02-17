from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/api/<b64_data>', methods=['GET'])
def hello(b64_data):

    decoded_data = base64.b64decode(b64_data).decode()
    result = say_hello(decoded_data)
    return result

def say_hello(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run()