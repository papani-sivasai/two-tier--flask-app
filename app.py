import os
from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', ''),
    'port': int(os.getenv('DB_PORT', 3306))
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM todos ORDER BY id DESC')
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task', '').strip()
    if task:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO todos (task) VALUES (%s)', (task,))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE todos SET completed = NOT completed WHERE id = %s', (todo_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit(todo_id):
    new_task = request.form.get('new_task', '').strip()
    if new_task:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE todos SET task = %s WHERE id = %s', (new_task, todo_id))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
