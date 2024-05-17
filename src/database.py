# database.py

import sqlite3

class Database:
    """
    Manages the creation and manipulation of an SQLite database.

    Arguments
    ---------
    db_path:  The path of the database.

    """
    def __init__(self, 
                 db_path: str = 'src/data/database.db') -> None:
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """
        Creates the database and connects to it.

        """
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table(self) -> None:
        """
        Creates the table for storing Brownian motions.
        
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS brownian_motions (
                id INTEGER PRIMARY KEY,
                motion_data BLOB
            );
        ''')
        self.connection.commit()

    def insert_brownian_motion(self, motion_data: bytes) -> None:
        """
        Inserts a Brownian motion into the database table.

        Arguments
        ---------
        motion_data :  The Brownian motion data.
        
        """
        self.cursor.execute(
            'INSERT INTO brownian_motions (motion_data) VALUES (?)', 
            (motion_data,)
        )
        self.connection.commit()

    def fetch_all_brownian_motions(self) -> list:
        """
        Fetches all Brownian motions stored inside the database.

        Returns
        -------
        All the Brownian motions.
        
        """
        self.cursor.execute('SELECT motion_data FROM brownian_motions')
        return self.cursor.fetchall()
    
    def clear(self) -> None:
        """
        Clears the database from all its data.

        """
        self.cursor.execute('DELETE FROM brownian_motions')
        self.connection.commit()

    def close(self) -> None:
        """
        Closes that databse connection.
        
        """
        self.cursor.close()
        self.connection.close()
