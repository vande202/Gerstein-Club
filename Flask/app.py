from flask import Flask,render_template,url_for
import sqlite3
import db


app = Flask(__name__)


@app.route('/')
def test():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()