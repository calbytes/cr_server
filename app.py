from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

@app.route('/get_quote')
def get_quote():
    return 'GetQuote!\n'

@app.route('/post_contact_message')
def post_contact_message():
    return 'message posted!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')