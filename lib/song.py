from config import CONN, CURSOR
from . import CONN, CURSOR
class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    @classmethod
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY,
        name TEXT,
        album TEXT
)
"""

CURSOR.execute(sql)
pass