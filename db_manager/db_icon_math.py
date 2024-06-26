import psycopg
from .config import ICON_MATH_DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
from enum import Enum, auto

config = ICON_MATH_DB_CONFIG

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

# APIs for IconMath Keywords
def get_keywords_by_content_id(data):
    row = execute(psql.GET_KEYWORDS_BY_ID, Fetch.ONE, data)
    return row
