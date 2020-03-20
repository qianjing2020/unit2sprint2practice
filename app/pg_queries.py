import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

dbname = os.getenv("dbname", default="OOPS")
user = os.getenv("user", default="OOPS")
password = os.getenv("password", default="OOPS") 
host = os.getenv("host", default="OOPS")

conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)

conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

dir(conn)

cur = conn.cursor()

### An example query
cur.execute('SELECT * from charactercreator_character;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchone()
print(result)