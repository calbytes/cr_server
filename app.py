from flask import Flask, jsonify, request
import db_manager.db as db
import auth.utils as utils
from datetime import datetime

app = Flask(__name__)

@app.route('/keywords', methods = ['GET'])
def get_keywords():
    if(request.method == 'GET'):
        try:
            keywords = db.get_keywords_by_content_id()
            json = request.get_json()
            id = json.get('id')
            keywords = db.get_keywords_by_content_id(id)
            keys = ['keywords']
            response = dict(zip(keys, keywords))
            return jsonify(keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 404 

@app.route('/indexIP', methods = ['POST'])
def index_ip():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            ip = json.get('ip')
            current_ts = datetime.now()
            data = ip, current_ts
            db.insert_index_ip(data)
            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500 

@app.route('/quote', methods = ['GET', 'POST'])
def get_quote():
    if(request.method == 'GET'):
        try:
            quote = db.get_random_quote()
            keys = ['quote', 'author', 'title']
            quote_dict = dict(zip(keys, quote))
            return jsonify(quote_dict)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 404 
    
@app.route('/contact', methods = ['POST'])
def contact():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            name = json.get('name')
            email = json.get('email')
            message = json.get('message')
            ip = json.get('ip')
            current_ts = datetime.now()
            data = name, email, message, current_ts, ip
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
            email = json.get('email')
            password = json.get('password')
            ip = json.get('ip')
            current_ts = datetime.now()
            data = username, email, password, current_ts, ip
            db.insert_signup_entry(data)
            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500 

@app.route('/cnetLogin', methods = ['POST'])
def login():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            username = json.get('username')
            password = json.get('password')
            ip = json.get('ip')

            is_auth = utils.verify_login_attempt(username, password)
            if is_auth:
                return jsonify({'status': 'success', 'role': 'USER'}), 200
            else:
                print('user %s not authenticated' % username)
                return jsonify({'status': '401'}), 401
            
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500
        
#TODO
@app.route('/logout', methods = ['POST'])
def logout():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            username = json.get('username')
            password = json.get('password')
            ip = json.get('ip')

            is_auth = utils.verify_login_attempt(username, password)
            if is_auth:
                return jsonify({'status': 'success', 'role': 'USER'}), 200
            else:
                print('user %s not authenticated' % username)
                return jsonify({'status': '401'}), 401
            
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')