from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        t = request.form['text']

        conn = sqlite3.connect("mss.db")
        cursor = conn.cursor()
        if t == "":
            print("Пустая строка")
            conn = sqlite3.connect("mss.db")
            cursor = conn.cursor()
            with conn:
                cursor.execute("SELECT * FROM users ORDER BY id DESC")
                rows = cursor.fetchall()
            conn.close()
            return render_template("index.html", mass=rows)
        else:
            with conn:
                cursor.execute("INSERT INTO users (mass) values(?)", (t,))
                cursor.execute("SELECT * FROM users ORDER BY id DESC")
                rows = cursor.fetchall()

            conn.close()

            return render_template("index.html", mass=rows)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)