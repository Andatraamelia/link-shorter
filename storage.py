# работа с БД
import sqlite3

conn = sqlite3.connect("links.db")

conn.execute('''
CREATE TABLE IF NOT EXISTS links(
    key  VARCHAR(7) PRIMARY KEY,
    link TEXT
)
''')
conn.commit()

def add_link(key: str, link: str) -> None:
    conn.execute(
        "INSERT INTO links (key, link) VALUES (?, ?)",
        (key, link)
    )
    conn.commit()