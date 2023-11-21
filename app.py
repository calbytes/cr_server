from flask import Flask, jsonify, request
import db_manager.db as db

app = Flask(__name__)

@app.route('/quote', methods = ['GET', 'POST'])
def get_quote():
    if(request.method == 'GET'):
        quote = db.get_selected_quote()[0]
        print('--->>> ' + str(quote))
        keys = ['quote', 'author', 'title']
        quote_dict = dict(zip(keys, quote))
        return jsonify(quote_dict)
    
    
'''
@app.route('/contact', methods = ['POST'])
def contact():
    return ''

@app.route('/signup', methods = ['POST'])
def signup():
    if(request.method == 'POST'):
        record = json.loads(request.data)
        db.create_user
    return ''

@app.route('/cnetLogin', methods = ['POST'])
def login():
    if(request.method == 'POST'):
        request
    return ''

@app.route('/indexIP', methods = ['POST'])
def indexIP():
    if(request.method == 'POST'):
    return ''
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')