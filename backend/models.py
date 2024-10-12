import sqlite3

def get_db_conection():
    conn = sqlite3.connect('store.db')
    conn.row_factory = sqlite3.row
    return conn

def get_products():
    conn = get_db_conection()
    products = conn.execute('SELECT * FROM products')
     conn.close()
     return products

def add_product(name, description,price,stock):
    conn = get_db_conection()
    conn.execute(
        'INSER INTO products(name,description,price,stock) VALUES (?,?,?,?)',(name,description, price stock))
        conn.comit()
        conn.close()
