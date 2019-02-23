from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

def setup(dbfile, event_emitter):
    # check that db exists if not create one


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
 
    return None
