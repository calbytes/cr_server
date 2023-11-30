import psycopg
from .config import DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
import random
from enum import Enum, auto

config = DB_CONFIG

class Fetch(Enum):
    ONE = auto()
    ALL = auto()
    EXC = auto()

def execute(psql_raw, fetch: Fetch, params=None):
    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(psql_raw, params)

                if fetch == Fetch.ONE:
                    row = cur.fetchone()
                    return row
                elif fetch == Fetch.ALL:
                    rows = cur.fetchall()
                    return rows
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


#APIs for /login
def get_db_pwd_hash(username):
    execute(psql.GET_USER_PWD_HASH, Fetch.ONE, (username,))


#APIs for /signup
def add_signup_entry(data):
    execute(psql.CREATE_SIGNUP_ENTRY, Fetch.EXC, data)

#APIs for /contact
def create_contact_form(data):
    execute(psql.INSERT_CONTACT_ENTRY, Fetch.EXC, data)

# APIs for /quote 
def get_random_quote():
    rows = execute(psql.SELECT_UNSELECTED_QUOTES, Fetch.ALL)
    random_num = random.randrange(len(rows))
    quote_id = rows[random_num][0]
    execute(psql.UPDATE_QUOTE_SELECTED, 
            Fetch.EXC, 
            (quote_id,))
    quote = execute(psql.SELECT_QUOTE_BY_ID, 
                    Fetch.ONE, 
                    (quote_id,))
    return quote

def get_selected_quote():
    quote_id = execute(psql.SELECT_LAST_QUOTE_ID, Fetch.ONE)[0]
    quote = execute(psql.SELECT_QUOTE_BY_ID, 
                    Fetch.ONE, 
                    (quote_id,))
    return quote