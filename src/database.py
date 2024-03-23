# database.py

import sqlite3

class Database:
    def __init__(self, db_path='src/data/database.db'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS brownian_motions (
                id INTEGER PRIMARY KEY,
                motion_data BLOB
            );
        ''')
        self.connection.commit()

    def insert_brownian_motion(self, motion_data):
        self.cursor.execute('INSERT INTO brownian_motions (motion_data) VALUES (?)', (motion_data,))
        self.connection.commit()

    def fetch_all_brownian_motions(self):
        self.cursor.execute('SELECT motion_data FROM brownian_motions')
        return self.cursor.fetchall()
    
    def clear(self):
        self.cursor.execute('DELETE FROM brownian_motions')
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
