import db_manager.db as db

def verify_login_attempt(username, user_pwd):
    #TODO
    #db_hash = db.get_db_pwd_hash(username)
    #user_input_hash = hash_str(password)

    data = (username,)
    db_pwd = db.get_user_pwd(data)[0]

    if user_pwd == db_pwd:
        return True
    else:
        return False

def hash_str(password):
    #TODO
    return 'pwd_hash'