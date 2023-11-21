import psycopg
from .config import DB_CONFIG
from webapp.psql_queries import PSQL_QUERIES as psql
 
config = DB_CONFIG

def get_selected_quote():
    quote_id = get_data(psql.SELECT_LAST_QUOTE_ID)[0]
    quote = get_data(psql.SELECT_QUOTE_BY_ID, quote_id)
    return quote

def get_data(psql_raw, params=None, single_row=True):
    with psycopg.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(psql_raw, params)

            if single_row:
                rows = cur.fetchall()
                return rows
            else:
                row = cur.fetchone()
                return row
            
