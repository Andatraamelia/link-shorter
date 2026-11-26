# работа с БД
import sqlite3

conn = sqlite3.connect('links.db', check_same_thread=False)

conn.execute('''
CREATE TABLE IF NOT EXISTS links(
    key  VARCHAR PRIMARY KEY,
    link TEXT
)
''')
conn.commit()

def add_link(key: str, link: str) -> bool: # Добавляет ссылку в ДБ, возвращает успех или провал трназакции
    try:
        conn.execute(
            "INSERT INTO links (key, link) VALUES (?, ?)",
            (key, link)
        )
        conn.commit()

        return True

    except sqlite3.IntegrityError:
        return False


def clear() -> bool: # очистить все записи
    conn.execute(
        """
        DELETE FROM links;
        """
    )
    conn.commit()

    return True


def find(elem: str) -> list: # Найти конкретную запись по ключу или ссылке
    return conn.execute(
        "SELECT * FROM links WHERE link = ? OR key = ?",
        (elem, elem),
    ).fetchall()


def show() -> list: # показать все записи в БД
    return conn.execute(
        "SELECT * FROM links"
    ).fetchall()


def delete(elem) -> bool: # очистить все записи
    try: # Отрабатываем, если всё хорошо
        conn.execute(
            """
            DELETE FROM links
            WHERE link = ? OR key = ?;
            """, (elem,elem),
        )
        conn.commit()
        return True
    
    except Exception as error: # выводим ошибку, если возникает, возвращаем фолс
        print(f'smthn gone wrong: {error}')
        return False