from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pymysql
import pymysql.cursors, os

app = Flask(__name__)

conn = cursor = None

def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="userlyno", database="crud_dbmysql")
    cursor = conn.cursor()

def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@app.route("/")
@app.route("/main")
def main():
    openDb()
    container = []
    sql = "SELECT * FROM stikom"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('home.html', container=container)

if __name__ == "__main__":
    app.run()
