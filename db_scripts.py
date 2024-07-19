import db_manager.db as db

def add_entitlements():
    email = 'mo.jahama@gmail.com'
    role = 'IconMath_REVIEWER'
    resource = 'IconMath'
    data = (email, role, resource)
    db.add_entitlements(data)
    print('added entitlements: ' + str(data))

def get_entitlements():
    email = 'caalla3@gmail.com'
    data = (email,)
    entitlements = db.get_user_entitlements(data)
    print(entitlements)

if __name__ == '__main__':
    print("STARTING db_scripts")
    add_entitlements()
    print("FINISHED db_scripts")