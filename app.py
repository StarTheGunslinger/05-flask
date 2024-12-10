from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            un= request.form['un']
            pwd= request.form['pwd']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO login (un, pwd) VALUES (?,?)",(un,pwd))
                con.commit()
                msg = "Record successfully added"
        except:
            #con.rollback()
            msg="error in insert operation" + " " + un + " " + pwd
        finally:
            return render_template("result.html", msg=msg)
            con.close()

    

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from login")
    rows = cur.fetchall()
    return render_template('list.html',rows=rows)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        try:
            un= request.form['un']
            pwd= request.form['pwd']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                try:
                    sqlite_insert_query = """SELECT * from login where username ='""" + un + """' and password = '""" + pwd + """'"""
                    cur.execute(sqlite_insert_query)
                    records = cur.fetchall()
                    if (len(records) >= 1):
                        msg = "Bingo" + " " + str(records)
                    else:
                        msg = "Nope"
                except:
                    msg = "Nope2"
        
        except:
            msg="error in insert operation"
        finally:
            return render_template("result.html", msg=msg)
            con.close()

if __name__ == "__main__":
    app.run()