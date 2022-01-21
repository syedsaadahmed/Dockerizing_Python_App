from flask import Flask
import os
import socket
import mysql.connector

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return "Hello World with Python Flask!"

@app.route('/')
def hello():
    html = "<h3>Hello World from {hostname}!</h3>"
    html += "<h3>Your random word is: {random_word}</h3>"
    db = mysql.connector.connect(
              host=os.getenv("MYSQL_SERVICE_HOST"),
              port=os.getenv("MYSQL_SERVICE_PORT"),
              user="root",
              passwd=os.getenv("MYSQL_DB_PASSWORD"),
              database="pyapplicationdb",
              auth_plugin="mysql_native_password"
         )
    cursor = db.cursor()
    cursor.execute("select word from random_words order by rand() limit 1;")
    res = cursor.fetchall()
    return html.format(random_word=res[0][0], hostname=socket.gethostname())