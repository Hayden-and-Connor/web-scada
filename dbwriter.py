from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

def setup(dbfile, event_emitter):
    # check that db exists if not create one
    conn = create_connection(dbfile)
    with conn:
    	create_tables(conn)
    conn.close()
    
    @event_emitter.on('data_new')
    def save_data(name, val, ts):
        print(val)
        conn = create_connection(dbfile)
        with conn:
            create_data(conn, (name, val, ts))
            conn.close()

    # add other db writers

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_tables(conn):
	sql_data_table = """ CREATE TABLE IF NOT EXISTS data (
                                        rowid integer PRIMARY KEY,
                                        name text NOT NULL,
                                        value text NOT NULL
                                        timestamp text NOT NULL
                                    ); """
    create_table(conn, sql_data_table)

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_data(conn, data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO data(name, value, timestamp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid