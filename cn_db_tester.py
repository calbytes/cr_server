import db_manager.db as db

def test_db():
    quote = db.get_random_quote()
    print(str(quote))



if __name__ == '__main__':
    test_db()