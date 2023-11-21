class PSQL_QUERIES:

    SELECT_LAST_QUOTE_ID = '''
        SELECT quote_id
        FROM selected_quotes
        ORDER BY timestamp DESC
        LIMIT 1;
    '''

    SELECT_QUOTE_BY_ID = '''
        SELECT quote, author, title 
        FROM quotes 
        WHERE id = %s;
    '''