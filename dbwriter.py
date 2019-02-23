from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

def setup(dbfile, event_emitter, event_type):
    # check that db exists if not create one


    @event_emitter.on(event_type)
    def save_data(name, val, ts):
        print val
        conn = create_connection(dbfile)
        with conn:
            create_data(conn, (name, val, ts))
