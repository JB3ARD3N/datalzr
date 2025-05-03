import sqlite3
from config import DATABASE_PATH

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS trends (
            id INTEGER PRIMARY KEY,
            source TEXT,
            timestamp REAL,
            keyword TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_data(entries):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.executemany('INSERT INTO trends (source, timestamp, keyword, content) VALUES (?, ?, ?, ?)',
                  [(e['source'], e['timestamp'], e['keyword'], e['content']) for e in entries])
    conn.commit()
    conn.close()

def fetch_data(start_time, end_time):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM trends WHERE timestamp BETWEEN ? AND ?', (start_time, end_time))
    results = c.fetchall()
    conn.close()
    return results
