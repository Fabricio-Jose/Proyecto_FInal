import sqlite3

DB_PATH = "erpdiff.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS changes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file TEXT,
        change TEXT,
        suggestion TEXT
    )''')
    conn.commit()
    conn.close()

def save_change(file, change, suggestion):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO changes (file, change, suggestion) VALUES (?, ?, ?)''',
                   (file, change, suggestion))
    conn.commit()
    conn.close()