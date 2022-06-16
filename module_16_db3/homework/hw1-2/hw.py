import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

CREATE_dir_TABLE = """
DROP TABLE IF EXISTS 'director';
CREATE TABLE 'director' (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_second_name TEXT VARCHAR(50) NOT NULL
) 
"""
CREATE_movie_TABLE = """
DROP TABLE IF EXISTS 'movie';
CREATE TABLE 'movie' (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_titlr VARCHAR(50) NOT NULL
) 
"""
CREATE_actor_TABLE = """
DROP TABLE IF EXISTS 'actors';
CREATE TABLE 'actors' (
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50) NOT NULL
    act_last_name VARCHAR(50) NOT NULL
    act_gender VARCHAR(1) NOT NULL
) 
"""


CREATE_movie_direction_TABLE = """
DROP TABLE IF EXISTS 'movie_direction';
CREATE TABLE 'movie_direction' (
    dir_id INTEGER,
    mov_id INTEGER,
    FOREIGN KEY(dir_id) REFERENCES director(dir_id) ON DELETE CASCADE 
    FOREIGN KEY(mov_id) REFERENCES movie(movie_id) ON DELETE CASCADE 
  
) 
"""
CREATE_oscar_awarded_TABLE = """
DROP TABLE IF EXISTS 'oscar_awarded';
CREATE TABLE 'oscar_awarded' (
    award_id INTEGER,
    mov_id INTEGER,
    FOREIGN KEY(mov_id) REFERENCES movie(movie_id) ON DELETE CASCADE  
    
) 
"""

CREATE_moviecast_TABLE = """
DROP TABLE IF EXISTS 'movie_cast';
CREATE TABLE 'movie_cast' (
    act_id INTEGER,
    mov_id INTEGER,
    role VARCHAR(50),
    FOREIGN KEY(act_id) REFERENCES actors(act_id) ON DELETE CASCADE 
    FOREIGN KEY(mov_id) REFERENCES movie(movie_id) ON DELETE CASCADE 
  
) 
"""



def create_tables():
    with sqlite3.connect("new.db") as conn:
        cursor = conn.cursor()

        cursor.executescript(ENABLE_FOREIGN_KEY)
        cursor.executescript(CREATE_dir_TABLE)
        cursor.executescript(CREATE_movie_TABLE)
        cursor.executescript(CREATE_actor_TABLE)
        cursor.executescript(CREATE_movie_direction_TABLE)
        cursor.executescript(CREATE_oscar_awarded_TABLE)
        cursor.executescript(CREATE_moviecast_TABLE)


if __name__ == '__main__':
    create_tables()