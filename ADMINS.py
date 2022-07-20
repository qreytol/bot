import sqlite3

class ADMcommand():
    '''Підключення до ДБ адмінів'''
    def __init__(self, database):
        '''Підключення до ДБ'''
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        
    def check_adm(self, user_id):
        '''Перевірка Адмінки'''
        return self.c.execute("SELECT adm FROM users WHERE user_id = ?", (user_id, )).fetchone()
    
    def plus_adm(self, user_id):
        '''+ Адмінка'''
        self.c.execute("UPDATE users SET adm = 1 WHERE user_id = ?", (user_id, ))
        self.conn.commit()

    def plus_two_adm(self, user_id):
        '''++ Адмінка'''
        self.c.execute("UPDATE users SET adm = 2 WHERE user_id = ?", (user_id, ))
        self.conn.commit()
        
    def plus_three_adm(self, user_id):
        '''+++ Адмінка'''
        self.c.execute("UPDATE users SET adm = 3 WHERE user_id = ?", (user_id, ))
        self.conn.commit()
        
    def plus_four_adm(self, user_id):
        '''++++ Адмінка'''
        self.c.execute("UPDATE users SET adm = 4 WHERE user_id = ?", (user_id, ))
        self.conn.commit()
        
    def plus_five_adm(self, user_id):
        '''+++++ Адмінка'''
        self.c.execute("UPDATE users SET adm = 5 WHERE user_id = ?", (user_id, ))
        self.conn.commit()
        
    def minus_adm(self, user_id):
        '''-адмінка'''
        self.c.execute('UPDATE users SET adm = 0 WHERE user_id = ?', (user_id, ))
        self.conn.commit()



  
#        if 'Слот ' in message.text:
#            user_id_money = message.from_user.id
#            slot_symma = int(message.text[4:])
#            check_money_score_start = (db.slot(user_id_money)[0])
#            start_score = random.choice(slot_emoji)
#            start_random_win = int(random.choice(random_win))
#            check_money_score_otrizite = db.slot(user_id_money)[0]
#            if bool(check_money_score_start) == True and check_money_score_otrizite.isdigit() == True:
#                if check_money_score_start >= slot_symma:
#                    if start_score == '1':
#                        slot_symma_plus = check_money_score_start + (slot_symma * start_random_win)
#                        slot_symma_pokaz_plus = slot_symma * (start_random_win)
#                        db.new_score(slot_symma_plus, user_id_money)
#                        check_money_score = db.slot(user_id_money)[0]
#                        await message.reply(f'[😁](tg://user?id={user_id_money})Ти виграв!!!\n📈 +{slot_symma_pokaz_plus}$\n💸Тепер в тебе: {check_money_score}$', parse_mode='Markdown')
#                    elif start_score == '2':
#                        slot_symma_minus = check_money_score_start - (slot_symma * 2)
#                        slot_symma_pokaz_minus = slot_symma * 2
#                        db.new_score(slot_symma_minus, user_id_money)
#                        check_money_score = db.slot(user_id_money)[0]
#                        await message.reply(f'[😢](tg://user?id={user_id_money})Ти програв(((\n📉 -{slot_symma_pokaz_minus}$\n💸Тепер в тебе: {check_money_score}$', parse_mode='Markdown')
#                else:
#                    await message.reply('В тебе немає такої сумми!!')
#            else:
#                await message.reply('В тебе мінусове число(')
