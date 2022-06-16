import sqlite3
from typing import List


DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]


class Book:

    def __init__(self, id: int, title: str, author: str, count:int):
        self.id = id
        self.title = title
        self.author = author
        self.count=count

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                'CREATE TABLE `table_books`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author,count INTEGER  DEFAULT 0 )'
            )
            cursor.executemany(
                'INSERT INTO `table_books` '
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
            )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from `table_books`')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]

def check_one_book(title,author)->bool:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM table_books WHERE title=? and author=?""",(title,author,))
        result=cursor.fetchone()
        if result:
            return True
        else:
            return False

def add_bookss(title,author) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO `table_books` (title, author) VALUES(?,?)',(title,author,))
def update_count(title,author) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE `table_books` SET count = count + 1  WHERE title =? and author=?;',(title,author,))

def bookss_by_author(author) ->List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM `table_books` WHERE author=? ',(author,))
        result=cursor.fetchall()
        return [Book(*row) for row in result]


