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

def execute(psql_raw, fetch: Fetch, params=None):
    with psycopg.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(psql_raw, params)

            if fetch == Fetch.ONE:
                row = cur.fetchone()
                return row
            elif fetch == Fetch.ALL:
                rows = cur.fetchall()
                return rows
            
#TODO write function to update data, set quote.selected = TRUE. can get_data do