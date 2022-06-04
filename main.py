from email import message
from itertools import count
import logging
from types import NoneType
from aiogram import Bot, Dispatcher, executor, types
import time
from datetime import datetime
from translate import Translator

from aiohttp import ContentTypeError

#підключення бота
bot = Bot(token='5370746338:AAFz2g5B_HTHMVFVmsOOzvpmSKRDnz3KaQQ')
#Диспетчер для  бота
dp = Dispatcher(bot) 

@dp.message_handler(content_types='text')
async def rp_commands(message: types.Message):    
    if message.text == 'youid':
        youid = message.reply_to_message.from_user.id
        await bot.send_message(message.chat.id, youid)
    if message.text.lower() == 'дата':
        dt = datetime.now()
        locd = dt.strftime('%H')
        locd = int(locd)
        locd += 3
        locdt = dt.strftime('%M')
        loc = time.localtime()
        day = time.strftime('%A', loc)
        mes = time.strftime('%B', loc)
        chislo = time.strftime('%d', loc)
        meschislo = time.strftime('m', loc)
        fulldata = time.strftime('%d:%m:%Y', loc)
        tran = Translator(from_lang='english', to_lang='uk')
        tranday = tran.translate(day)
        tranmes = tran.translate(mes)
        await bot.send_message(message.chat.id, (f'⌚️ Час: {locd}:{locdt}\n⏰ День: {tranday}\n📅 Дата: {chislo} | {tranmes}\n⏳ Фулл дата: {fulldata}'))
        pass
    if message.text.lower() == 'уроки':
        n = time.localtime()
        now = datetime.now()
        den_nedeli = datetime.weekday(now)
        mnt = time.strftime('%H%M%S', n)
        if den_nedeli == 0:
            if mnt <= '141500':
                await bot.send_message(message.chat.id, '''
1) 9:30 - 10:00 - Англ. Мова
2!) 10:10 - 10:40 - Фіз. Вих.
3) 10:50 - 11:20 - Математика
4) 11:30 - 12:00 - Географія
5) 12:15 - 12:45 - Іст. України
6) 13:00 - 13:30 - Укр. Літ
7) 13:40 - 14:10 - Нім. Мова''')
        if den_nedeli == 1:
            if mnt <= '141500':
                await bot.send_message(message.chat.id, '''
1) 9:30 - 10:00 - Англ. Мова
2) 10:10 - 10:40 - Фізика
3) 10:50 - 11:20 - Заруб. Літ
4) 11:30 - 12:00 - Укр. Мова
5) 12:15 - 12:45 - Математика
6) 13:00 - 13:30 - Біологія
7) 13:40 - 14:10 - Основи Здоров'я''')
        if den_nedeli == 2:
            if mnt <= '141500':
                await bot.send_message(message.chat.id, '''
1) 9:30 - 10:00 - Географія
2) 10:10 - 10:40 - Хімія
3!)10:50 - 11:20 - Фіз. Вих
4) 11:30 - 12:00 - Математика
5) 12:15 - 12:45 - Іст. України
6) 13:00 - 13:30 - Всесв. Історія
7) 13:40 - 14:10 - Мистецтво''')
        if den_nedeli == 3:
            if mnt <= '145500':
                await bot.send_message(message.chat.id, '''
1) 9:30 - 10:00 - Укр. Мова
2) 10:10 - 10:40 - Фізика
3) 10:50 - 11:20 - Заруб. Літ
4) 11:30 - 12:00 - Укр. Літ
5!) 12:15 - 12:45 - Фіз. Вих
6) 13:00 - 13:30 - Біологія
7) 13:40 - 14:10 - Христ. Етика
8!) 14:20 - 14:50 - Труд. Навчання''')
        if den_nedeli == 4:
            if mnt <= '141500':
                await bot.send_message(message.chat.id, '''
1) 9:30 - 10:00 - Інформатика(1)
2) 10:10 - 10:40 - Інформатика(1)
3) 10:50 - 11:20 - Хімія
4) 11:30 - 12:00 - Математика
5) 12:15 - 12:45 - Англ. Мова
6) 13:00 - 13:30 - Нім. Мова
7) 13:40 - 14:10 - Інформатика(2)''')
            else:
                await bot.send_message(message.chat.id, 'Не знаю нащо тобі розклад... Но вже по урокам')
        if den_nedeli == 5:
            await bot.send_message(message.chat.id, 'Сьоні вихідні!!!')
        if den_nedeli == 6:
            await bot.send_message(message.chat.id, 'Сьоні вихідні!!!')
    
    if message.text == 'my':
        await bot.send_message(message.chat.id, message.from_user.id)
    if message.text == 'mychat':
        await bot.send_message(message.chat.id, message.chat.id)
    if message.text == 'Лив':
        await bot.leave_chat(message.chat.id)
    if message.text == 'Get_chat_member_count:test': 
        chtid = message.chat.id
        count = await bot.get_chat_members_count(chtid)
        await bot.send_message(chtid, count)
    if message.text.lower() == '//':
        await bot.send_message(message.chat.id, )
    if message.reply_to_message:
        a = message.from_user.first_name
        b = message.from_user.id
        c = message.reply_to_message.from_user.first_name
        d = message.reply_to_message.from_user.id
        if message.text.lower() == 'зїсти':
            await bot.send_message(message.chat.id, f"😅😋| [{a}](tg://user?id={b}) з'їв [{c}](tg://user?id={d})", parse_mode='Markdown')
                
        if message.text.lower() == "погладити":
            await bot.send_message(message.chat.id, f"🥺🤭| [{a}](tg://user?id={b}) погладив [{c}](tg://user?id={d})", parse_mode='Markdown')
            
        if message.text.lower() == "вбити":
            await bot.send_message(message.chat.id, f"😡🔪| [{a}](tg://user?id={b}) вбив [{c}](tg://user?id={d})", parse_mode='Markdown')
                        
        if message.text.lower() == "вдарити":
            await bot.send_message(message.chat.id, f"😡👎🏿| [{a}](tg://user?id={b}) вдарив [{c}](tg://user?id={d})", parse_mode='Markdown')
                        
        if message.text.lower() == "поцілувати":
            await bot.send_message(message.chat.id, f"😏😘| [{a}](tg://user?id={b}) поцілував [{c}](tg://user?id={d})", parse_mode='Markdown')
                        
        if message.text.lower() == "кусь":
            await bot.send_message(message.chat.id, f"😋| [{a}](tg://user?id={b}) кусьнув [{c}](tg://user?id={d})", parse_mode='Markdown')
            
        if message.text.lower() == "спалити":
            await bot.send_message(message.chat.id, f"🤬🔥| [{a}](tg://user?id={b}) спалив [{c}](tg://user?id={d})", parse_mode='Markdown')
            
        if message.text.lower() == "уєбати":
            await bot.send_message(message.chat.id, f"😈👊| [{a}](tg://user?id={b}) дуже сильно вдарив [{c}](tg://user?id={d})", parse_mode='Markdown')    
            
        if message.text.lower() == "кохатися":
            await bot.send_message(message.chat.id, f"🥵❤️| [{a}](tg://user?id={b}) жостко кохається з [{c}](tg://user?id={d})", parse_mode='Markdown')
        
        if message.text.lower() == "цьом":
            await bot.send_message(message.chat.id, f"💓🌸| [{a}](tg://user?id={b}) поцьомав [{c}](tg://user?id={d})", parse_mode='Markdown')
        
        if message.text.lower() == 'дати підсрачника':
            await bot.send_message(message.chat.id, f"🦶☺️| [{a}](tg://user?id={b}) дав підсрачника [{c}](tg://user?id={d})", parse_mode='Markdown')
            
if __name__ == '__main__':
    #запуск бота
    executor.start_polling(dp, skip_updates=True)
