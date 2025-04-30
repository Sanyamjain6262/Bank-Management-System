import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self._init_db()
    
    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS accounts (account_no TEXT PRIMARY KEY, customer_name TEXT NOT NULL, balance REAL DEFAULT 0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, account_no TEXT, type TEXT, amount REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
        self.conn.commit()
    
    def log_transaction(self, account_no, trans_type, amount):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (?, ?, ?)", (account_no, trans_type, amount))
        self.conn.commit()
