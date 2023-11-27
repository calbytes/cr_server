import db_manager.db as db

def verify_login_attempt(username, password):
    db_hash = db.get_db_pwd_hash(username)
    user_input_hash = hash_str(password)
    #TODO
    if db_hash == user_input_hash:
        return True
    else:
        return False

def hash_str(password):
    #TODO
    return 'pwd_hash'