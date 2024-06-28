import db_manager.db_icon_math as dbim

def test_db():
    id = 1
    data = (id,)
    keywords = dbim.get_keywords_by_content_id(data)
    print(str(keywords))


if __name__ == '__main__':
    test_db()