from ast import Await
from cgitb import text
from email import message, utils
from email.policy import default
from itertools import count
import logging
from tabnanny import check
from types import NoneType
from typing import final
from xml.dom import ValidationErr
from aiogram import Bot, Dispatcher, executor, types
import time
import datetime
import aiogram
from click import command
from numpy import integer
from DBusers import SQLitedb
from DATETIME import date_time
import random
from ADMINS import ADMcommand
import config
import requests
from bs4 import BeautifulSoup as BS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import keyboard as inl

from aiohttp import ContentTypeError

#
slot_emoji = ['1', '2']

#
random_win = [2, 1.25, 1.5, 1.75]

#підключення до дати
dtime = date_time()

#підключає БД
db = SQLitedb('users.db')

#Підключення до БД адмінів
admbd = ADMcommand('users.db')

#підключення бота
bot = Bot(token='5370746338:AAFz2g5B_HTHMVFVmsOOzvpmSKRDnz3KaQQ')

#Диспетчер для  бота
dp = Dispatcher(bot) 

#Додає нового юзера чата
@dp.message_handler(content_types=['new_chat_members'])
async def new_members_handler(message: types.Message):
    new_member = message.new_chat_members
    new_member = new_member[0].id
    if not db.check_user(new_member):
        db.add_to_db(new_member)
    await bot.send_message(message.chat.id, new_member)

#при команді /start перевіряє чи є юзер в БД, якщо немає то його додає
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    add_time = dtime.time(time.localtime())
    username = message.from_user.username
    firstname = message.from_user.first_name
    if not db.check_nick(user_id):
        db.add_to_db(user_id, username, firstname)
        db.add_datetime(add_time, user_id)
    await bot.send_message(message.chat.id, f'''
👨‍🔧Привіт [{firstname}](tg://user?id={user_id})

🤖мене звати Петька 

😊Моя головна задача приглядувати за вашим чатом!!

📝написавши команду `Допомога`, ти можеш дізнатись всі мої команди''', parse_mode='Markdown')

@dp.message_handler(content_types='text')
async def rp_commands(message: types.Message):
    try:
        if 'Погода ' in message.text:
            
            city = message.text[7:]
            split = city.split()
            city_ok = '-'.join(split)
        
            url = 'https://ua.sinoptik.ua/погода-' + city_ok
            r = requests.get(url)
            html = BS(r.content, 'lxml')

            for el in html.select('#content'):
                t_min = el.select('.temperature .min')[0].text
                t_max = el.select('.temperature .max')[0].text
                min_text = el.select('.weatherIco')[0]['title']
                day_pars = el.select('.day-link')[0].text
                month_pars = el.select('.date')[0].text
                day_name = el.select('.month')[0].text
                zaraz = el.select('.imgBlock .today-temp')[0].text
                witer_rano = el.select('.gray .p4')[2].text
                witer_den = el.select('.gray .p5')[2].text
                witer_vechir = el.select('.gray .p7')[2].text
                dosch_rano = el.select('tr .p3')[7].text
                dosch_den = el.select('tr .p5')[7].text
                dosch_vechir = el.select('tr .p7')[7].text
                
            await message.reply(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}\n⛱️Зараз: {zaraz}\n☀️Рано:\nВітер | {witer_rano} м/сек\nЙмовірність опадів | {dosch_rano}%\n🌤️День:\nВітер | {witer_den} м/сек\nЙмовірність опадів | {dosch_den}%\n⭐Вечір:\nВітер | {witer_vechir} м/сек\nЙмовірність опадів | {dosch_vechir}%', reply_markup=inl.mainMenu)
            
            @dp.callback_query_handler(text='right_weather')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(days=2)
                dt_zavtra = zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[1].text
                    t_max = el.select('.temperature .max')[1].text
                    min_text = el.select('.weatherIco')[1]['title']
                    day_pars = el.select('.day-link')[1].text
                    month_pars = el.select('.date')[1].text
                    day_name = el.select('.month')[1].text
                    witer_rano = el.select('.gray .p4')[2].text
                    witer_den = el.select('.gray .p6')[2].text
                    witer_vechir = el.select('.gray .p8')[2].text
                    dosch_rano = el.select('tr .p4')[7].text
                    dosch_den = el.select('tr .p6')[7].text
                    dosch_vechir = el.select('tr .p8')[7].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}\n☀️Рано:\nВітер | {witer_rano} м/сек\nЙмовірність опадів | {dosch_rano}%\n🌤️День:\nВітер | {witer_den} м/сек\nЙмовірність опадів | {dosch_den}%\n⭐Вечір:\nВітер | {witer_vechir} м/сек\nЙмовірність опадів | {dosch_vechir}%', reply_markup=inl.mainMenu)
                
            @dp.callback_query_handler(text='left_weather')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                pisla_zavtra = today + datetime.timedelta(days=3)
                dt_zavtra = pisla_zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[2].text
                    t_max = el.select('.temperature .max')[2].text
                    min_text = el.select('.weatherIco')[2]['title']
                    day_pars = el.select('.day-link')[2].text
                    month_pars = el.select('.date')[2].text
                    day_name = el.select('.month')[2].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}', reply_markup=inl.mainMenu)
            
            @dp.callback_query_handler(text='thourbtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(days=4)
                dt_zavtra = zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[3].text
                    t_max = el.select('.temperature .max')[3].text
                    min_text = el.select('.weatherIco')[3]['title']
                    day_pars = el.select('.day-link')[3].text
                    month_pars = el.select('.date')[3].text
                    day_name = el.select('.month')[3].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}', reply_markup=inl.mainMenu)
            
            @dp.callback_query_handler(text='fivebtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(days=5)
                dt_zavtra = zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[4].text
                    t_max = el.select('.temperature .max')[4].text
                    min_text = el.select('.weatherIco')[4]['title']
                    day_pars = el.select('.day-link')[4].text
                    month_pars = el.select('.date')[4].text
                    day_name = el.select('.month')[4].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}', reply_markup=inl.mainMenu)
            
            @dp.callback_query_handler(text='sixbtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(days=6)
                dt_zavtra = zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[5].text
                    t_max = el.select('.temperature .max')[5].text
                    min_text = el.select('.weatherIco')[5]['title']
                    day_pars = el.select('.day-link')[5].text
                    month_pars = el.select('.date')[5].text
                    day_name = el.select('.month')[5].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}', reply_markup=inl.mainMenu)
            
            @dp.callback_query_handler(text='twobtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(days=1)
                dt_zavtra = zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                for el in html.select('#content'):
                    t_min = el.select('.temperature .min')[0].text
                    t_max = el.select('.temperature .max')[0].text
                    min_text = el.select('.weatherIco')[0]['title']
                    day_pars = el.select('.day-link')[0].text
                    month_pars = el.select('.date')[0].text
                    day_name = el.select('.month')[0].text
                    zaraz = el.select('.imgBlock .today-temp')[0].text
                    witer_rano = el.select('.gray .p4')[2].text
                    witer_den = el.select('.gray .p5')[2].text
                    witer_vechir = el.select('.gray .p7')[2].text
                    dosch_rano = el.select('tr .p3')[7].text
                    dosch_den = el.select('tr .p5')[7].text
                    dosch_vechir = el.select('tr .p7')[7].text
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура: {t_min} | {t_max}\n⛱️Зараз: {zaraz}\n☀️Рано:\nВітер | {witer_rano} м/сек\nЙмовірність опадів | {dosch_rano}%\n🌤️День:\nВітер | {witer_den} м/сек\nЙмовірність опадів | {dosch_den}%\n⭐Вечір:\nВітер | {witer_vechir} м/сек\nЙмовірність опадів | {dosch_vechir}%', reply_markup=inl.mainMenu)
            
        if message.text == 'Допомога' or message.text == 'допомога':
            user_id = message.from_user.id
            await message.reply(f'''
[📒](tg://user?id={user_id})На данний момент в мене є такі команди

👌Основні:
1) +ник | +нік
2) Дата
3) бан | кик | мут - тільки адміни можуть юзати
4) !адмінка [реплай до юзера]
5) Погода [місто] | приклад: Погода львів
6) +опис 

😊РП:
1) `дати підсрачника`
2) `зїсти`
3) `погладити`
4) `поцілувати`
5) `кохатися`
6) `вбити`
7) `кусь`
8) `спалити`
9) `сильно вдарити`
10) `цьом`
''', parse_mode='Markdown')
        if message.text == 'Хто я':
            my_user_id = message.from_user.id
            new_opis_check = db.check_opis(my_user_id)
            await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐️ Статус адмінки: {admbd.check_adm(my_user_id)[0]}\n💬 Мій опис: ' + new_opis_check[0] + '\n\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0])
        if '+нік ' in message.text or '+ник ' in message.text:
            user_id = message.from_user.id
            nickname = message.text[5:]
            db.nick_user(nickname, user_id)
            new_nick_check = db.check_nick(user_id)
            await bot.send_message(message.chat.id, '📒Твій новий нік: ' + new_nick_check[0])
        if '+опис ' in message.text:
            user_id = message.from_user.id
            nickname = message.text[6:]
            db.opis_user(nickname, user_id)
            new_opis_check = db.check_opis(user_id)
            await bot.send_message(message.chat.id, '📝Твій новий опис: ' + new_opis_check[0])
        if message.text == 'твій айді' or message.text == 'Твій айді':
            youid = message.reply_to_message.from_user.id
            await bot.send_message(message.chat.id, youid)  
        if message.text.lower() == 'дата':
            loc = time.localtime()
            locd = time.strftime('%H', loc)
            locdt = time.strftime('%M', loc)
            week = time.strftime('%A', loc)
            month = time.strftime('%B', loc)
            chislo = time.strftime('%d', loc)
            fulldata = time.strftime('%d:%m:%Y', loc)
            await bot.send_message(message.chat.id, (f'⌚️ Час: {locd}:{locdt}\n⏰ День: {dtime.transweek(week)}\n📅 Дата: {chislo} | {dtime.transmonth(month)}\n⏳ Фулл дата: {fulldata}'))
        if message.text == 'Мій айді' or message.text == 'мій айді':
            #Вертає айді того хто то написав
            await bot.send_message(message.chat.id, f'`{message.from_user.id}`', parse_mode='Markdown')
        if message.text == 'Мій нік' or message.text == 'мій нік':
            #Вертає нік пользователя з бд 
            user_id = message.from_user.id
            user_firstname = message.from_user.first_name
            nick_us = db.check_nick(user_id)[0]
            await message.reply(f'👤Нік користувача [{user_firstname}](tg://user?id={user_id}) ' + nick_us, parse_mode='Markdown')
        if message.text == 'Твій нік' or message.text == 'твій нік':
            #Вертає нік зареплеєного пользователя з бд 
            user_id_reply_to = message.reply_to_message.from_user.id
            user_firstname_reply = message.reply_to_message.from_user.first_name
            user_id_reply_to_to = message.reply_to_message.from_user.id
            nick_us_reply = db.check_nick(user_id_reply_to)[0]
            await bot.send_message(message.chat.id, f'👤Нік користувача [{user_firstname_reply}](tg://user?id={user_id_reply_to_to}) ' + nick_us_reply, parse_mode='Markdown')
        if message.text == 'Айді чата':
            #вертає айді чата
            await message.reply(f'`{message.chat.id}`', parse_mode='Markdown')
        if message.text == 'Лив':
            #бот ліває з группи
            await bot.leave_chat(message.chat.id)
        if message.reply_to_message:
            add_time = dtime.time(time.localtime())
            user_id_reply = message.reply_to_message.from_user.id
            firstname_reply = message.reply_to_message.from_user.first_name
            username_reply = message.reply_to_message.from_user.username
            if not db.check_id_bool(user_id_reply):
                db.add_to_db(user_id_reply, username_reply, firstname_reply)
                db.add_datetime(add_time, user_id_reply)
                
            if db.check_nick(user_id_reply) == None:
                db.nick_user(firstname_reply, user_id_reply)
                
            username = message.from_user.username
            user_id = message.from_user.id
            nick_first_user = db.check_nick(user_id)[0]
            b = message.from_user.id
            d = message.reply_to_message.from_user.id
            nick_two_user = db.check_nick(d)[0]
            opis_rp = message.text
            adm_check_adm = admbd.check_adm(d)[0]
            check_adm = admbd.check_adm(message.from_user.id)[0]
            if message.text == '!адмінка':
                if check_adm >= 1:
                    if adm_check_adm == 1:
                        admbd.plus_adm(d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: 1 рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text == '!!адмінка':
                if check_adm >= 1:
                    if adm_check_adm == 2:
                        admbd.plus_two_adm(d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: 2 рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text == '!!!адмінка':
                if check_adm >= 1:
                    if adm_check_adm == 3:
                        admbd.plus_three_adm(d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: 3 рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text == '!!!!адмінка':
                if check_adm >= 1:
                    if adm_check_adm == 4:
                        admbd.plus_four_adm(d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: 4 рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text == '!!!!!адмінка':
                if check_adm >= 1:
                    if adm_check_adm == 5:
                        admbd.plus_five_adm(d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: 5 рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text.lower() == 'зїсти':
                await bot.send_message(message.chat.id, f"😅😋| [{nick_first_user}](tg://user?id={b}) з'їв [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
        
            if message.text.lower() == "погладити":
                await bot.send_message(message.chat.id, f"🥺🤭| [{nick_first_user}](tg://user?id={b}) погладив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text.lower() == "вбити":
                await bot.send_message(message.chat.id, f"😡🔪| [{nick_first_user}](tg://user?id={b}) вбив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text.lower() == "вдарити":
                await bot.send_message(message.chat.id, f"😡👎🏿| [{nick_first_user}](tg://user?id={b}) вдарив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text.lower() == "поцілувати":
                await bot.send_message(message.chat.id, f"😏😘| [{nick_first_user}](tg://user?id={b}) поцілував [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text.lower() == "кусь":
                await bot.send_message(message.chat.id, f"😋| [{nick_first_user}](tg://user?id={b}) кусьнув [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text.lower() == "спалити":
                await bot.send_message(message.chat.id, f"🤬🔥| [{nick_first_user}](tg://user?id={b}) спалив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text.lower() == "сильно вдарити":
                await bot.send_message(message.chat.id, f"😈👊| [{nick_first_user}](tg://user?id={b}) дуже сильно вдарив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')    
            
            if message.text.lower() == "кохатися":
                await bot.send_message(message.chat.id, f"🥵❤️| [{nick_first_user}](tg://user?id={b}) жостко кохається з [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
        
            if message.text.lower() == "цьом":
                await bot.send_message(message.chat.id, f"💓🌸| [{nick_first_user}](tg://user?id={b}) поцьомав [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                
            if message.text.lower() == 'дати підсрачника':
                await bot.send_message(message.chat.id, f"🦶☺️| [{nick_first_user}](tg://user?id={b}) дав підсрачника [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
    except TypeError:
        add_time = dtime.time(time.localtime())
        user_id = message.from_user.id
        username = message.from_user.username
        firstname = message.from_user.first_name
        if not db.check_id_bool(user_id):
            db.add_to_db(user_id, username, firstname)
            db.add_datetime(add_time, user_id)
        
        if db.check_nick(user_id) == None:
            db.nick_user(firstname, user_id)
    except UnboundLocalError:
        await message.reply('Такого міста не існує')
    
        
if __name__ == '__main__':
    #запуск бота
    executor.start_polling(dp, skip_updates=True)
