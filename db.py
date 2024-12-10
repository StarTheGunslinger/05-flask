#%%
import sqlite3

conn = sqlite3.connect("database.db")
print("opened db with sucess")

conn.execute("CREATE TABLE login (un TEXT, pwd TEXT)")
print("table created sucessfully")

conn.close()
