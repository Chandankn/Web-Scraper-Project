import sqlite3

def connect():
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS AMAZON_SHOPPING (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")

    print("Table crated successfully!")
    
    conn.close()
    
def insert_into_table(dbname.values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO AMAZON_SHOPPING (NAME, ADDRESS, PRICE, AMENTITES,RATING) VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql ,values)

    conn = commit()
    conn.close()
    
def get_shopping_info(dbname):
    conn = sqlite3.connect(dbname)
  
cur = conn.cursor()

cur.execute("SELECE * FRAOM AMAZON_SHOPPING")


table_data = cur.fetchall()

for record in table_data:
    print(record)
    
conn.close()    
