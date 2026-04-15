from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('inventory.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS inventory
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 quantity INTEGER,
                 price REAL)''')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('inventory.db')
    data = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('index.html', items=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    quantity = request.form['quantity']
    price = request.form['price']

    conn = sqlite3.connect('inventory.db')
    conn.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
                 (name, quantity, price))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
