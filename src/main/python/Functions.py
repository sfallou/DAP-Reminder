import datetime

import sqlite3
 
from sqlite3 import Error

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "mydatabase.db")

def sql_connection():
    try:
        con = sqlite3.connect(db_path)
        return con
    except sqlite3.Error:
        print(sqlite3.Error)
 
def create_dap(pn,cmm,rev_cmm,dap,rev_dap,comments):
	con = sql_connection()
	date = datetime.datetime.now().strftime('%d/%m/%Y')
	deadline = (datetime.date.today() + datetime.timedelta(3*365/12)).strftime('%d/%m/%Y')
	cursor = con.cursor()
	query = ''' INSERT INTO cmm( pn, cmm, rev_cmm, dap, rev_dap, date_creation, deadline, comments )
	    	        VALUES ( ?,?,?,?,?,?,?,? ) '''
	cursor.execute(query,(pn,cmm,rev_cmm,dap,rev_dap,date,deadline,comments))
	con.commit()
	con.close()


def delete_dap(index):
	pass

def show_dap():
	con = sql_connection()
	cursor = con.cursor()
	query = ''' SELECT * FROM cmm '''
	cursor.execute(query)
	all_rows = cursor.fetchall()
	con.commit()
	con.close()
	return all_rows

def deadline(deadline):
	color = (0,250,0)
	isodeadline = datetime.datetime.strptime(deadline, '%d/%m/%Y')
	remain = isodeadline - datetime.datetime.today()
	if (remain.days > 60):
		color = (0,250,0)
	elif (remain.days <= 60 and remain.days >= 30):
		color = (0,0,250)
	else:
		color = (250,0,0)
	return remain.days,color


if __name__ == '__main__':
	## test deadline()
	print(deadline("10/11/2019")[0])
	## INSERT VALUES 
	#for i in range(50):
	#	create_dap("128933","21-10-32","Rev 04","DAP345544","Rev 01","Un commentaire")
	## Show VALUES
	datas = show_dap()
	for data in datas:
		print(data)




