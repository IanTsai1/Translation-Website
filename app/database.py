import sqlite3

import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            fromLang TEXT,
            toLang TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insertDefault():
    conn = sqlite3.connect('database.db') #establishes connection to database
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM records')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute('INSERT INTO records (fromLang, toLang) VALUES (?, ?)', ("detected_language", "spanish"))
    else:
        cursor.execute('UPDATE records SET fromLang=?, toLang=?', ("detected_language", "spanish"))

    conn.commit()
    conn.close()

def update_fromLang(fromLang):
    conn = sqlite3.connect('database.db') #establishes connection to database
    cursor = conn.cursor()

    cursor.execute('UPDATE records SET fromLang=?', (fromLang,))

    conn.commit()
    conn.close()

def update_toLang(toLang):
    conn = sqlite3.connect('database.db') #establishes connection to database
    cursor = conn.cursor()

    cursor.execute('UPDATE records SET toLang=?', (toLang,))

    conn.commit()
    conn.close()

def getLang():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT fromLang, toLang FROM records')
    record = cursor.fetchone()

    conn.close()

    if record:
        fromLang, toLang = record
        return fromLang, toLang

    return None, None

def clear_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM records')

    conn.commit()
    conn.close()