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

#APIs for /indexIP
def insert_index_ip(data):
    execute(psql.INSERT_INDEX_IP, Fetch.EXC, data)

#APIs for /login
def get_user_pwd(data):
    row = execute(psql.GET_USER_PWD, Fetch.ONE, data)
    return row

#APIs for /signup
def insert_signup_entry(data):
    execute(psql.INSERT_SIGNUP_ENTRY, Fetch.EXC, data)

#APIs for /contact
def insert_contact_entry(data):
    execute(psql.INSERT_CONTACT_ENTRY, Fetch.EXC, data)

# APIs for /quote 
def get_random_quote():
    rows = execute(psql.SELECT_UNSELECTED_QUOTES, Fetch.ALL)
    if len(rows) == 5:
        reset_selected_quotes()
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

def reset_selected_quotes():
    execute(psql.RESET_SELECTED_QUOTES,
            Fetch.EXC)