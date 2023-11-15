from flask import Flask

app = Flask(__name__)

@app.route('/get_quote')
def get_quote():
    return 'Hello, Flask!\n'

@app.route('/post_contact_message')
def post_contact_message():
    return 'message posted!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)