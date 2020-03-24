import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists book (id INTEGER PRIMARY KEY, title text, author text, year integer, serial_no integer)")
    conn.commit()
    conn.close()
     
def insert(title,author,year,serial_no):  
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,serial_no))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
     
def search(title="",author="",year="",serial_no=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR serial_no=?",(title,author,year,serial_no))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()
 
def update(id,title,author,year,serial_no):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,serial_no=? WHERE id=?",(title,author,year,serial_no,id))
    conn.commit()
    conn.close()

