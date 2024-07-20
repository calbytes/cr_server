import db_manager.db as db

def verify_login_attempt(email, user_pwd):
    #TODO
    #db_hash = db.get_db_pwd_hash(username)
    #user_input_hash = hash_str(password)

    data = (email,)

    try:
        db_pwd = db.get_user_pwd(data)[0]
        if user_pwd == db_pwd:
            return True
    except:
        print("error in pwd verification")        

    return False

def hash_str(password):
    #TODO
    return 'pwd_hash'