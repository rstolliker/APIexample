import sqlite3 as sql 

# database management helper functions
# global variables
CONN = sql.connect("messages.db")
CUR = CONN.cursor()


def initialize_table():
    """Will create Messages table in database.
    If the table already exists, it will be deleted.
    Use with caution."""
    CUR.execute("DROP TABLE IF EXISTS Messages")
    CUR.execute("CREATE TABLE Messages(mid integer PRIMARY KEY AUTOINCREMENT, sysplat varchar(60), sysver varchar(6), msg varchar(120))")
    CONN.commit()

def insert_vals(plat: str, ver: str, msg: str = ""):
    """Wrapper to insert row into Messages.
       Takes a "message" to make testing easier."""
    CUR.execute("INSERT INTO Messages (sysplat, sysver, msg) VALUES (?, ?, ?)", (plat, ver, msg[:120]))
    CONN.commit()

def all_vals():
    """Wrapper to return messages as a list"""
    return CUR.execute("SELECT * FROM Messages").fetchall()

