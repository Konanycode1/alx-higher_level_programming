#!/usr/bin/python3
'''this script connect to a database '''
import MySQLdb
import sys
if __name__ == '__main__':
    
    db = MySQLdb.connect(
        host = 'localhost',
        port =3306,
        user = sys.argv[1],
        pswd = sys.argv[2],
        db = sys.argv[3]
    )

    cursor_db = db.cursor()
    cursor_db.excute("SELECT id, name FROM states ORDER BY id")
    rows = cursor_db.fetchall()
for row in rows:
    print(row)

cursor_db.close()
db.close()


