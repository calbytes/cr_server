class PSQL_QUERIES:

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

    INSERT_CONTACT_ENTRY = '''
        INSERT INTO contact_messages
        (name, email, message, timestamp, ip)
        VALUES
        (%s, %s, %s, %s, %s)
    '''

    INSERT_SIGNUP_ENTRY = '''
        INSERT INTO signup_entries
        (username, email, password, timestamp, ip)
        VALUES
        (%s, %s, %s, %s, %s)
    '''

    GET_USER_PWD = '''
        SELECT password 
        FROM signup_entries 
        WHERE email = %s;
    '''

    INSERT_INDEX_IP = '''
        INSERT INTO index_ips
        (ip_address, timestamp)
        VALUES
        (%s, %s)
    '''

    RESET_SELECTED_QUOTES = '''
        UPDATE quotes
        SET selected = false
        WHERE selected = true; 
    '''

    GET_USER_ENTITLEMENTS = '''
        SELECT role
        FROM entitlements
        WHERE email = %s;
    '''

    INSERT_ENTITLEMENTS = '''
        INSERT INTO entitlements
        (email, role, resource)
        VALUES
        (%s, %s, %s)
    '''

    GET_USERNAME = '''
        SELECT username
        FROM signup_entries
        WHERE email = %s;
    '''

    # Pool Ledger 

    SELECT_POOL_PLAYER_STATS = '''
        SELECT *
        FROM pool_player_stats
    '''

    SELECT_SCORESHEET_IDS = '''
        SELECT file_id
        FROM pool_files
        WHERE file_id != 0
		ORDER BY file_id;
    '''

    SELECT_POOL_FILE = '''
        SELECT file_data
        FROM pool_files
        WHERE file_name = %s;
    '''