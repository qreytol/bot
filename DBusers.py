import sqlite3
import time
import random

class SQLitedb():
    '''Клас для роботи з базою данних'''
    def __init__(self, database):
        '''Підключення до ДБ'''
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
    
    def add_to_db(self, user_id, username, nicknames):
        '''Додає айді и юзернейм до БД'''
        self.c.execute("INSERT INTO users ('user_id', 'username', 'nick') VALUES (?, ?, ?)", (user_id, username, nicknames, ))
        self.conn.commit()
        
    def check_user(self, user_id, username):
        '''Провіряє чи є айді и юзер в БД'''
        return bool(self.c.execute("SELECT * FROM users WHERE user_id = ? AND username = ?", (user_id, username)).fetchone())
    
    def nick_user(self, nickname, user_id):
        '''Міняє внутрішній нік бота'''
        self.c.execute('UPDATE users SET nick = ? WHERE user_id = ?', (nickname, user_id, ))
        self.conn.commit()
        
    def check_nick(self, user_id):
        '''Перевіряє нік для РП команд'''
        return self.c.execute('SELECT nick FROM users WHERE user_id = ?', (user_id, )).fetchone()

    def check_opis(self, user_id):
        '''Перевіряє опис для РП команд'''
        return self.c.execute('SELECT opisanie FROM users WHERE user_id = ?', (user_id, )).fetchone()

    def opis_user(self, nickname, user_id):
        '''Міняє внутрішній опис бота'''
        self.c.execute('UPDATE users SET opisanie = ? WHERE user_id = ?', (nickname, user_id, ))
        self.conn.commit()

    def check_nick_bool(self, user_id):
        '''Перевіряє нік для РП вертає тру фоллс команд'''
        return bool(self.c.execute('SELECT nick FROM users WHERE user_id = ?', (user_id, )).fetchone())
    
    def check_id(self, user_id):
        '''Провіряє чи є айдів БД'''
        self.c.execute("SELECT * FROM users WHERE user_id = ?", (user_id, )).fetchone()
        
    def check_id_bool(self, user_id):
        '''Провіряє чи є айдів БД BOOL'''
        return bool(self.c.execute("SELECT * FROM users WHERE user_id = ?", (user_id, )).fetchone())
        
    def add_datetime(self, date, user_id):
        '''Додає дату добавлення користувача'''
        self.c.execute('UPDATE users SET date = ? WHERE user_id = ?', (date, user_id, )).fetchone()
        self.conn.commit()
    
    def check_datetime(self, user_id):
        '''Перевіряє коли користувач був доданий в БД'''
        return self.c.execute('SELECT date FROM users WHERE user_id = ?', (user_id, )).fetchone()
        
    def check_id_username(self, username):
        return (self.c.execute('SELECT user_id FROM users WHERE username = ?', (username, )).fetchone())
    
    def full_users(self):
        return(self.c.execute('SELECT * FROM users')).fetchall()
    
