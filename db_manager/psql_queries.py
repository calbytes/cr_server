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

    SELECT_UNSELECTED_QUOTES = '''
        SELECT id 
        FROM quotes 
        WHERE selected = 'false';
    '''

    UPDATE_QUOTE_SELECTED = '''
        UPDATE quotes 
        SET selected = TRUE 
        WHERE id = %s;
    '''

    #TODO
    CREATE_CONTACT_ENTRY = '''
        INSERT INTO contact_table
        (name, email, message, ip)
        VALUES
        (%s, %s, %s, %s)
    '''