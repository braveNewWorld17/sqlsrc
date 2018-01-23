import MySQLdb

db = MySQLdb.connect(host="172.31.18.133",    # your host, usually localhost
                     user="simplestep",         # your username
                     passwd="as920558",  # your password
                     db="SimpleStep")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM USER")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
