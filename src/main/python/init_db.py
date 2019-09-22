import datetime

import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except sqlite3.Error:
        print(sqlite3.Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS cmm(id integer PRIMARY KEY AUTOINCREMENT, pn text, cmm text, rev_cmm text, dap text, rev_dap text, date_creation text, deadline text, comments text)")
    con.commit()
    con.close()

def init():
	con = sql_connection()
	sql_table(con)


if __name__ == '__main__':
	init()


