import psycopg2


conn = psycopg2.connect(database='linkedindb', user='josh', host='PostgresServer', password='linkedin')

cur = conn.cursor()

string  = 'CREATE TABLE users IF NOT EXIST(\
			ID serial primary key,\
			email varchar(40),\
			firstname varchar(30),\
			lastname varchar(30)\
			)'	
cur.execute(string)
conn.commit()
