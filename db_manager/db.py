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

def get_user_entitlements(data):
    row = execute(psql.GET_USER_ENTITLEMENTS, Fetch.ONE, data)
    return row[0]

#APIs for /signup
def insert_signup_entry(data):
    execute(psql.INSERT_SIGNUP_ENTRY, Fetch.EXC, data)

#APIs for /contact
def insert_contact_entry(data):
    execute(psql.INSERT_CONTACT_ENTRY, Fetch.EXC, data)

# APIs for /quote 
def get_random_quote():
    rows = execute(psql.SELECT_UNSELECTED_QUOTES, Fetch.ALL)
    if len(rows) < 5:
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

def reset_selected_quotes():
    execute(psql.RESET_SELECTED_QUOTES, Fetch.EXC)
    
# User / Entitlements
def add_entitlements(data):
    execute(psql.INSERT_ENTITLEMENTS, Fetch.EXC, data)

def get_user_name(data):
    row = execute(psql.GET_USERNAME, Fetch.ONE, data)
    return row[0]


# Pool Stats / Ledger
def get_pool_player_stats():
    stats = execute(psql.SELECT_POOL_PLAYER_STATS, Fetch.ALL)
    return stats

def get_scoresheet_ids():
    rows = execute(psql.SELECT_SCORESHEET_IDS, Fetch.ALL)
    scoresheet_ids = [row[0] for row in rows]
    return scoresheet_ids

def get_pool_file():
    row = execute(psql.SELECT_POOL_FILE, Fetch.ONE)
    return row[0]
