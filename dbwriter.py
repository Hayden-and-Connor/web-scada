from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

class DBWriter:

def setup(dbfile, event_emitter, event_type):
    # check that db exists if not create one


    @event_emitter.on(event_type)
    def save_data(name, val, ts):
        conn = create_connection(dbfile)
        with conn:
            create_data(conn, (name, val, ts))
