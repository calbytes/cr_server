from flask import Flask, jsonify, request
import db_manager.db as db
import utils as utils
from datetime import datetime

app = Flask(__name__)

@app.route('/quote', methods = ['GET', 'POST'])
def get_quote():
    if(request.method == 'GET'):
        quote = db.get_random_quote()
        keys = ['quote', 'author', 'title']
        quote_dict = dict(zip(keys, quote))
        return jsonify(quote_dict)
    
@app.route('/contact', methods = ['POST'])
def contact():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            name = json.get('name')
            email = json.get('email')
            message = json.get('message')
            ip = json.get('ip')
            current_timestamp = datetime.now()
            data = name, email, message, current_timestamp, ip
            db.insert_contact_entry(data)
            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500 


@app.route('/signup', methods = ['POST'])
def signup():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            username = json.get('username')
            email = json.get('json')
            password = json.get('password')
            data = username, email, password
            db.add_signup_entry(data)
            #TODO
            return ''
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

@app.route('/cnetLogin', methods = ['POST'])
def login():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            username = json.get('username')
            password = json.get('password')
            access = utils.verify_login_attempt(username, password)
            if access:
                return 'ALLOW'
            else:
                return 'DENY'
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

@app.route('/indexIP', methods = ['POST'])
def indexIP():
    if(request.method == 'POST'):
        print('TODO')
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')