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

#підключення до дати
dtime = date_time()

#підключає БД
db = SQLitedb('users.db')

#Підключення до БД адмінів
admbd = ADMcommand('users.db')

#підключення бота
bot = Bot(token='5324556084:AAEg9g80LHMJVto9Gv2Cmahwl4bZ64MnQLk')

#Диспетчер для  бота
dp = Dispatcher(bot) 


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

🤖мене звати Арнольд 

😊Моя головна задача приглядувати за вашим чатом!!

📝написавши команду `Допомога`, ти зможеш дізнатись всі мої команди

Щоб добавити мене в свій чат натисни на кнопку нище⬇️''', reply_markup=inl.StartMenu, parse_mode='Markdown')

@dp.message_handler(content_types='text')
async def rp_commands(message: types.Message):
    try:
        if 'Погода ' in message.text:
            #показує детальну погоду з міста
            
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
                witer_den = el.select('.gray .p6')[2].text
                witer_vechir = el.select('.gray .p8')[2].text
                witer_nich = el.select('.gray .p2')[2].text
                dosch_rano = el.select('tr .p4')[7].text
                dosch_den = el.select('tr .p6')[7].text
                dosch_vechir = el.select('tr .p8')[7].text
                dosch_nich = el.select('tr .p2')[7].text
                dosch_rano = dosch_rano.replace('-', '0')
                dosch_den = dosch_den.replace('-', '0')
                dosch_vechir = dosch_vechir.replace('-', '0')
                dosch_nich = dosch_nich.replace('-', '0')
                temperatura_rano = el.select('.temperature .p4')[0].text
                temperatura_den = el.select('.temperature .p6')[0].text
                temperatura_vechir = el.select('.temperature .p8')[0].text
                temperatura_nich = el.select('.temperature .p2')[0].text
                mini_weather_rano = el.select('.img .p4 .weatherIco')[0]['title']
                mini_weather_den = el.select('.img .p6 .weatherIco')[0]['title']
                mini_weather_vechir = el.select('.img .p8 .weatherIco')[0]['title']
                mini_weather_nich = el.select('.img .p2 .weatherIco')[0]['title']
                
            await message.reply(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n⛱️Зараз: {zaraz}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
            
            
            @dp.callback_query_handler(text='right_weather')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(hours=3,days=1)
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
                    witer_nich = el.select('.gray .p2')[2].text
                    dosch_rano = el.select('tr .p4')[7].text
                    dosch_den = el.select('tr .p6')[7].text
                    dosch_vechir = el.select('tr .p8')[7].text
                    dosch_nich = el.select('tr .p2')[7].text
                    temperatura_rano = el.select('.temperature .p4')[0].text
                    temperatura_den = el.select('.temperature .p6')[0].text
                    temperatura_vechir = el.select('.temperature .p8')[0].text
                    temperatura_nich = el.select('.temperature .p2')[0].text
                    dosch_rano = dosch_rano.replace('-', '0')
                    dosch_den = dosch_den.replace('-', '0')
                    dosch_vechir = dosch_vechir.replace('-', '0')
                    dosch_nich = dosch_nich.replace('-', '0')
                    mini_weather_rano = el.select('.img .p4 .weatherIco')[0]['title']
                    mini_weather_den = el.select('.img .p6 .weatherIco')[0]['title']
                    mini_weather_vechir = el.select('.img .p8 .weatherIco')[0]['title']
                    mini_weather_nich = el.select('.img .p2 .weatherIco')[0]['title']
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
                
            @dp.callback_query_handler(text='left_weather')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                pisla_zavtra = today + datetime.timedelta(hours=3,days=2)
                dt_zavtra = pisla_zavtra.strftime('%Y-%m-%d')
                url = 'https://ua.sinoptik.ua/погода-' + city_ok + '/' + dt_zavtra
                r = requests.get(url)
                html = BS(r.content, 'lxml')
                check_number_pogoda = html.find('div', id='content').find('div', id='leftCol').find('div', id='mainContentBlock').find('div', id='blockDays').find('div', attrs={'class': 'tabsContent'}).find('div', attrs={'class': 'tabsContentInner'}).find('div', attrs={'class': 'Tab', 'id':'bd3c'}).find('div', attrs={'class': 'wMain clearfix'}).find('div', attrs={'class': 'rSide'}).find('table', attrs={'class': 'weatherDetails'}).find('tbody').find('tr', attrs={'class': 'temperature'}).find('td', attrs={'class': 'p5'})
                if check_number_pogoda == None:
                    for el in html.select('#content'):
                        t_min = el.select('.temperature .min')[2].text
                        t_max = el.select('.temperature .max')[2].text
                        min_text = el.select('.weatherIco')[2]['title']
                        day_pars = el.select('.day-link')[2].text
                        month_pars = el.select('.date')[2].text
                        day_name = el.select('.month')[2].text
                        witer_rano = el.select('.gray .p2')[2].text
                        witer_den = el.select('.gray .p3')[2].text
                        witer_vechir = el.select('.gray .p4')[2].text
                        witer_nich = el.select('.gray .p1')[2].text
                        dosch_rano = el.select('tr .p2')[7].text
                        dosch_den = el.select('tr .p3')[7].text
                        dosch_vechir = el.select('tr .p4')[7].text
                        dosch_nich = el.select('tr .p1')[7].text
                        temperatura_rano = el.select('.temperature .p2')[0].text
                        temperatura_den = el.select('.temperature .p3')[0].text
                        temperatura_vechir = el.select('.temperature .p4')[0].text
                        temperatura_nich = el.select('.temperature .p1')[0].text
                        dosch_rano = dosch_rano.replace('-', '0')
                        dosch_den = dosch_den.replace('-', '0')
                        dosch_vechir = dosch_vechir.replace('-', '0')
                        dosch_nich = dosch_nich.replace('-', '0')
                        mini_weather_rano = el.select('.img .p2 .weatherIco')[0]['title']
                        mini_weather_den = el.select('.img .p3 .weatherIco')[0]['title']
                        mini_weather_vechir = el.select('.img .p4 .weatherIco')[0]['title']
                        mini_weather_nich = el.select('.img .p1 .weatherIco')[0]['title']
                    
                    await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)

                else:
                    today = datetime.date.today()
                    pisla_zavtra = today + datetime.timedelta(hours=3,days=2)
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
                        witer_rano = el.select('.gray .p4')[2].text
                        witer_den = el.select('.gray .p6')[2].text
                        witer_vechir = el.select('.gray .p8')[2].text
                        witer_nich = el.select('.gray .p2')[2].text
                        dosch_rano = el.select('tr .p4')[7].text
                        dosch_den = el.select('tr .p6')[7].text
                        dosch_vechir = el.select('tr .p8')[7].text
                        dosch_nich = el.select('tr .p2')[7].text
                        temperatura_rano = el.select('.temperature .p4')[0].text
                        temperatura_den = el.select('.temperature .p6')[0].text
                        temperatura_vechir = el.select('.temperature .p8')[0].text
                        temperatura_nich = el.select('.temperature .p2')[0].text
                        dosch_rano = dosch_rano.replace('-', '0')
                        dosch_den = dosch_den.replace('-', '0')
                        dosch_vechir = dosch_vechir.replace('-', '0')
                        dosch_nich = dosch_nich.replace('-', '0')
                        mini_weather_rano = el.select('.img .p4 .weatherIco')[0]['title']
                        mini_weather_den = el.select('.img .p6 .weatherIco')[0]['title']
                        mini_weather_vechir = el.select('.img .p8 .weatherIco')[0]['title']
                        mini_weather_nich = el.select('.img .p2 .weatherIco')[0]['title']
                    
                    await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
                    
            
            @dp.callback_query_handler(text='thourbtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(hours=3,days=3)
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
                    witer_rano = el.select('.gray .p2')[2].text
                    witer_den = el.select('.gray .p3')[2].text
                    witer_vechir = el.select('.gray .p4')[2].text
                    witer_nich = el.select('.gray .p1')[2].text
                    dosch_rano = el.select('tr .p2')[7].text
                    dosch_den = el.select('tr .p3')[7].text
                    dosch_vechir = el.select('tr .p4')[7].text
                    dosch_nich = el.select('tr .p1')[7].text
                    temperatura_rano = el.select('.temperature .p2')[0].text
                    temperatura_den = el.select('.temperature .p3')[0].text
                    temperatura_vechir = el.select('.temperature .p4')[0].text
                    temperatura_nich = el.select('.temperature .p1')[0].text
                    dosch_rano = dosch_rano.replace('-', '0')
                    dosch_den = dosch_den.replace('-', '0')
                    dosch_vechir = dosch_vechir.replace('-', '0')
                    dosch_nich = dosch_nich.replace('-', '0')
                    mini_weather_rano = el.select('.img .p2 .weatherIco')[0]['title']
                    mini_weather_den = el.select('.img .p3 .weatherIco')[0]['title']
                    mini_weather_vechir = el.select('.img .p4 .weatherIco')[0]['title']
                    mini_weather_nich = el.select('.img .p1 .weatherIco')[0]['title']
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
            
            @dp.callback_query_handler(text='fivebtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(hours=3,days=4)
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
                    witer_rano = el.select('.gray .p2')[2].text
                    witer_den = el.select('.gray .p3')[2].text
                    witer_vechir = el.select('.gray .p4')[2].text
                    witer_nich = el.select('.gray .p1')[2].text
                    dosch_rano = el.select('tr .p2')[7].text
                    dosch_den = el.select('tr .p3')[7].text
                    dosch_vechir = el.select('tr .p4')[7].text
                    dosch_nich = el.select('tr .p1')[7].text
                    temperatura_rano = el.select('.temperature .p2')[0].text
                    temperatura_den = el.select('.temperature .p3')[0].text
                    temperatura_vechir = el.select('.temperature .p4')[0].text
                    temperatura_nich = el.select('.temperature .p1')[0].text
                    dosch_rano = dosch_rano.replace('-', '0')
                    dosch_den = dosch_den.replace('-', '0')
                    dosch_vechir = dosch_vechir.replace('-', '0')
                    dosch_nich = dosch_nich.replace('-', '0')
                    mini_weather_rano = el.select('.img .p2 .weatherIco')[0]['title']
                    mini_weather_den = el.select('.img .p3 .weatherIco')[0]['title']
                    mini_weather_vechir = el.select('.img .p4 .weatherIco')[0]['title']
                    mini_weather_nich = el.select('.img .p1 .weatherIco')[0]['title']
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
            
            @dp.callback_query_handler(text='sixbtn')
            async def weather_right(query: types.CallbackQuery):
                today = datetime.date.today()
                zavtra = today + datetime.timedelta(hours=3,days=5)
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
                    witer_rano = el.select('.gray .p2')[2].text
                    witer_den = el.select('.gray .p3')[2].text
                    witer_vechir = el.select('.gray .p4')[2].text
                    witer_nich = el.select('.gray .p1')[2].text
                    dosch_rano = el.select('tr .p2')[7].text
                    dosch_den = el.select('tr .p3')[7].text
                    dosch_vechir = el.select('tr .p4')[7].text
                    dosch_nich = el.select('tr .p1')[7].text
                    temperatura_rano = el.select('.temperature .p2')[0].text
                    temperatura_den = el.select('.temperature .p3')[0].text
                    temperatura_vechir = el.select('.temperature .p4')[0].text
                    temperatura_nich = el.select('.temperature .p1')[0].text
                    dosch_rano = dosch_rano.replace('-', '0')
                    dosch_den = dosch_den.replace('-', '0')
                    dosch_vechir = dosch_vechir.replace('-', '0')
                    dosch_nich = dosch_nich.replace('-', '0')
                    mini_weather_rano = el.select('.img .p2 .weatherIco')[0]['title']
                    mini_weather_den = el.select('.img .p3 .weatherIco')[0]['title']
                    mini_weather_vechir = el.select('.img .p4 .weatherIco')[0]['title']
                    mini_weather_nich = el.select('.img .p1 .weatherIco')[0]['title']
                    
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
            
            @dp.callback_query_handler(text='twobtn')
            async def weather_right(query: types.CallbackQuery):
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
                    witer_den = el.select('.gray .p6')[2].text
                    witer_vechir = el.select('.gray .p8')[2].text
                    witer_nich = el.select('.gray .p2')[2].text
                    dosch_rano = el.select('tr .p4')[7].text
                    dosch_den = el.select('tr .p6')[7].text
                    dosch_vechir = el.select('tr .p8')[7].text
                    dosch_nich = el.select('tr .p2')[7].text
                    dosch_rano = dosch_rano.replace('-', '0')
                    dosch_den = dosch_den.replace('-', '0')
                    dosch_vechir = dosch_vechir.replace('-', '0')
                    dosch_nich = dosch_nich.replace('-', '0')
                    temperatura_rano = el.select('.temperature .p4')[0].text
                    temperatura_den = el.select('.temperature .p6')[0].text
                    temperatura_vechir = el.select('.temperature .p8')[0].text
                    temperatura_nich = el.select('.temperature .p2')[0].text
                    mini_weather_rano = el.select('.img .p4 .weatherIco')[0]['title']
                    mini_weather_den = el.select('.img .p6 .weatherIco')[0]['title']
                    mini_weather_vechir = el.select('.img .p8 .weatherIco')[0]['title']
                    mini_weather_nich = el.select('.img .p2 .weatherIco')[0]['title']
                
                await query.message.edit_text(f'📅Дата: {day_pars} | {month_pars} | {day_name}\n📝Маленький опис: {min_text}\n🌡️Температура за весь день: {t_min} | {t_max}\n⛱️Зараз: {zaraz}\n☀️Ранок 9:00:\nВітер | {witer_rano} м/с\nЙмовірність опадів | {dosch_rano}%\nБуде: {mini_weather_rano}\nТемпература зранку: {temperatura_rano}\n🌤️День 15:00:\nВітер | {witer_den} м/с\nЙмовірність опадів | {dosch_den}%\nБуде: {mini_weather_den}\nТемпература вдень: {temperatura_den}\n⭐Вечір 21:00:\nВітер | {witer_vechir} м/с\nЙмовірність опадів | {dosch_vechir}%\nБуде: {mini_weather_vechir}\nТемпература ввечері: {temperatura_vechir}\n🌙Ніч 3:00:\nВітер | {witer_nich} м/с\nЙмовірність опадів | {dosch_nich}%\nБуде: {mini_weather_nich}\nТемпература вночі: {temperatura_nich}', reply_markup=inl.mainMenuTwo)
            
    
    except UnboundLocalError:
        await message.reply('Такого міста не існує')      
    
    try:
        if '!мут ' in message.text in message.text:
            user_id = message.from_user.id
            if  admbd.check_adm(user_id)[0] >= 2:
                d = message.reply_to_message.from_user.id
                time_myt = int(message.text.split()[1])
                na_chto_myt = message.text.split()[2]
                owner_adm = await bot.get_chat_member(message.chat.id, d)
                owner_adm = owner_adm.status
                if owner_adm == 'administrator' or owner_adm == 'creator':
                    await message.reply('Він адмін')
                elif message.reply_to_message.from_user.id == message.from_user.id:
                    await message.reply('Не можна себе мутити!')
                elif na_chto_myt == 'годин' or na_chto_myt == 'година':
                    full_minutes = datetime.datetime.now() + datetime.timedelta(hours=(time_myt+3))
                    fff = full_minutes.strftime('%Y-%m-%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, d, types.ChatPermissions(False), datetime.datetime.now() + datetime.timedelta(hours=time_myt))
                    await message.answer(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n⌚️Получив мут на: {time_myt} {na_chto_myt}\n⏳Юзер зможе писати в {fff}', parse_mode='Markdown')
                elif na_chto_myt == 'хвилин' or na_chto_myt == 'хвилина':
                    full_minutes = datetime.datetime.now() + datetime.timedelta(hours=3,minutes=time_myt)
                    fff = full_minutes.strftime('%Y-%m-%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, d, types.ChatPermissions(False), datetime.datetime.now() + datetime.timedelta(minutes=time_myt))
                    await message.answer(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n⌚️Получив мут на: {time_myt} {na_chto_myt}\n⏳Юзер зможе писати в {fff}', parse_mode='Markdown')
                elif na_chto_myt == 'днів' or na_chto_myt == 'день':
                    full_minutes = datetime.datetime.now() + datetime.timedelta(hours=3,days=time_myt)
                    fff = full_minutes.strftime('%Y-%m-%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, d, types.ChatPermissions(False), datetime.datetime.now() + datetime.timedelta(days=time_myt))
                    await message.answer(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n⌚️Получив мут на: {time_myt} {na_chto_myt}\n⏳Юзер зможе писати в {fff}', parse_mode='Markdown')
            else:
                await message.reply('в тебе немає таких прав')  
        if message.text == '!размут' or message.text == '!Размут' or message.text == '! размут' or message.text == '! Размут':
            d = message.reply_to_message.from_user.id
            get_user_inf = await bot.get_chat_member(message.chat.id, d)
            get_user_inf = get_user_inf.can_send_messages
            if get_user_inf == False:
                await bot.restrict_chat_member(message.chat.id, d, types.ChatPermissions(True,True,True,True,True,True))
                await message.answer(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n➕Тепер може говорити!', parse_mode='Markdown')
            else:
                await message.reply(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n➖Не мав мута')
        
        if message.text == '!бан' or message.text == '! бан' or message.text == '!Бан' or message.text == '! Бан':
            user_id = message.from_user.id
            if  admbd.check_adm(user_id)[0] >= 3:
                d = message.reply_to_message.from_user.id
                owner_adm = await bot.get_chat_member(message.chat.id, d)
                owner_adm = owner_adm.status
                if owner_adm == 'administrator' or owner_adm == 'creator':
                    await message.reply('Він адмін')
                elif d == message.from_user.id:
                    await message.reply('Не можна себе банити!')
                else:
                    await bot.ban_chat_member(message.chat.id, d)
                    await message.reply(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n➕Получив бан', parse_mode='Markdown')
            else:
                await message.reply('в тебе немає таких прав')    
        if message.text == '!разбан' or message.text == '!Разбан' or message.text == '! разбан' or message.text == '! Разбан':
            d = message.reply_to_message.from_user.id
            await bot.unban_chat_member(message.chat.id, d, True)
            await message.answer(f'👤Користувач [{db.check_nick(d)[0]}](tg://user?id={d})\n✖️Тепер може зайти!', parse_mode='Markdown')

        
    except IndexError:
        await message.reply('Ти неправильно ввів\nприклад: мут 1 година')
    except AttributeError:
        await message.reply('треба відповісти на юзера!')
    
    try:
        add_time = dtime.time(time.localtime())
        user_id = message.from_user.id
        username = message.from_user.username
        firstname = message.from_user.first_name
        if not db.check_id_bool(user_id):
            db.add_to_db(user_id, username, firstname)
            db.add_datetime(add_time, user_id)
        
        if db.check_nick(user_id) == None:
            db.nick_user(firstname, user_id)
            
        if 'Арнольд інфа ' in message.text or 'арнольд інфа ' in message.text:
            await message.reply(f'[🤔](tg://user?id={message.from_user.id}) я думаю, що ймовірність {random.randint(0,100)}%', parse_mode='Markdown')  
        
        if message.text == 'Хто я':
            #вертає інформацію про бота
            my_user_id = message.from_user.id
            new_opis_check = db.check_opis(my_user_id)
            check_adm_status = admbd.check_adm(my_user_id)[0]
            if check_adm_status == 0:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n╰ Арнольд інфа \nДля більш детальної інформації напишіть `Допомога`' , parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Простий учасник\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)
            elif check_adm_status == 1:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n╰ Арнольд інфа \nДля більш детальної інформації напишіть `Допомога`', parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Мл.адмін\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)
            elif check_adm_status == 2:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n╰ Арнольд інфа\nДля більш детальної інформації напишіть `Допомога`', parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Гл.адмін\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)
            elif check_adm_status == 3:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n├ Арнольд інфа\n╰ !Мут\nДля більш детальної інформації напишіть `Допомога`', parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Мл.модер\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)
            elif check_adm_status == 4:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('╰⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n├ Арнольд інфа \n├ !Мут\n╰ !Бан\nДля більш детальної інформації напишіть `Допомога`', parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Гл.модер\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)
            elif check_adm_status == 5:
                @dp.callback_query_handler(text='getCommands')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer('⭐Ви вмієте:\n├ +нік\n├ Дата\n├ Погода\n├ +опис\n├ Арнольд інфа\n├ !Мут\n├ !Бан\n╰ Получити БД\nДля більш детальної інформації напишіть `Допомога`', parse_mode='Markdown')
                    
                @dp.callback_query_handler(text='getOpis')
                async def weather_right(query: types.CallbackQuery):
                    await query.message.answer(f'⭐Твій опис: {db.check_opis(query.from_user.id)[0]}', parse_mode='Markdown')
                    
                await bot.send_message(message.chat.id, '👤 Мій нік: ' + db.check_nick(my_user_id)[0] + f'\n\n⭐Адмінка: {check_adm_status} рівня\n⌛Ранг: Творець\n📅 Вперше з нами появився в: ' + db.check_datetime(my_user_id)[0], reply_markup=inl.userKeyboard)

        if admbd.check_adm(message.from_user.id)[0] == 5 and message.text == 'Получити БД':
            for i in db.full_users():
                await message.reply(f'Ряд: {i[0]}\nАйді: {i[1]}\nЮзернейм: {i[2]}\nПол: {i[3]}\nНік: {i[4]}\nДата: {i[6]}\nСтатус АДМ: {i[7]}\nМісто: {i[8]}')
            
        if message.text == 'Допомога' or message.text == 'допомога':
            #Показує всі команди бота
            user_id = message.from_user.id
            await message.reply(f'''
[📒](tg://user?id={user_id})На данний момент в мене є такі команди

👌Основні:
1) +ник | +нік - міняє нік в самому боті
2) Дата | получаєш дату за теперішній час
3) бан | кік | мут - тільки адміни можуть юзати
4) +адмінка (рівень адмінки, з 1-5) [відповівши на користувача] | дає адмінку користувачу якому відповіли, приклад: +адмінка 3
5) Погода [місто] | приклад: Погода львів
6) +опис 
7) Арнольд інфа | приклад: Арнольд інфа мені йти їсти?
8) хто я | получиш інформацыю про себе (статус адмінки в боті, нік в боті, які команди ти вмієш використовувати)

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
11) `отруїти`
12) `покормити`
''', parse_mode='Markdown')
        if '+нік ' in message.text or '+ник ' in message.text:
            #міняє нік в боті
            user_id = message.from_user.id
            nickname = message.text[5:]
            db.nick_user(nickname, user_id)
            new_nick_check = db.check_nick(user_id)
            await bot.send_message(message.chat.id, '📒Твій новий нік: ' + new_nick_check[0])
        if '+опис ' in message.text:
            #міняє опис в боті
            user_id = message.from_user.id
            nickname = message.text[6:]
            db.opis_user(nickname, user_id)
            new_opis_check = db.check_opis(user_id)
            await bot.send_message(message.chat.id, '📝Твій новий опис: ' + new_opis_check[0])
        if message.text == 'твій айді' or message.text == 'Твій айді':
            #показує айді зареплаянного юзера
            youid = message.reply_to_message.from_user.id
            await bot.send_message(message.chat.id, youid)  
        if message.text.lower() == 'дата':
            #показує локальну дату
            loc = datetime.datetime.now() + datetime.timedelta(hours=3)
            locd = loc.strftime('%H')
            locdt = loc.strftime('%M')
            week = loc.strftime('%A')
            month = loc.strftime('%B')
            chislo = loc.strftime('%d')
            fulldata = loc.strftime('%d:%m:%Y')
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
            adm_check_adm = admbd.check_adm(d)[0]
            check_adm = admbd.check_adm(message.from_user.id)[0]
            
            if message.text == 'Гет' or message.text == 'гет':
                d = message.reply_to_message.from_user.id
                get_user_inf = await bot.get_chat_member(message.chat.id, d)
                get_user_inf = get_user_inf
                await message.reply(get_user_inf)
            if '+адмінка ' in message.text:
                #дає адмінку юзеру
                integer_for_adm_step = int(message.text[9:])
                if check_adm >= 1:
                    if adm_check_adm <= 5:
                        admbd.plus_adm(integer_for_adm_step, d)
                        await message.answer(f'👤Користувач [{nick_two_user}](tg://user?id={d})\n➕Получив доступ до Адмінки\n⚪Адмінка: {integer_for_adm_step} рівня', parse_mode='Markdown')
                    else:
                        await message.reply('Цей користувач вже має права на використання цієї команди')
                else:
                    await message.reply('В тебе нема прав на використання такої команди(')

            if message.text == 'зїсти' or message.text == 'Зїсти':
                await bot.send_message(message.chat.id, f"😅😋| [{nick_first_user}](tg://user?id={b}) з'їв [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                  
            if message.text == "погладити" or message.text == 'Погладити':
                await bot.send_message(message.chat.id, f"🥺🤭| [{nick_first_user}](tg://user?id={b}) погладив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text == "вбити" or message.text == 'Вбити':
                await bot.send_message(message.chat.id, f"😡🔪| [{nick_first_user}](tg://user?id={b}) вбив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text == "вдарити" or message.text == 'Вдарити':
                await bot.send_message(message.chat.id, f"😡👎🏿| [{nick_first_user}](tg://user?id={b}) вдарив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text == "поцілувати" or message.text == 'Поцілувати':
                await bot.send_message(message.chat.id, f"😏😘| [{nick_first_user}](tg://user?id={b}) поцілував [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                        
            if message.text == "кусь" or message.text == 'Кусь':
                await bot.send_message(message.chat.id, f"😋| [{nick_first_user}](tg://user?id={b}) кусьнув [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text == "спалити" or message.text == 'Спалити':
                await bot.send_message(message.chat.id, f"🤬🔥| [{nick_first_user}](tg://user?id={b}) спалив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text == "сильно вдарити" or message.text == 'Сильно вдарити':
                await bot.send_message(message.chat.id, f"😈👊| [{nick_first_user}](tg://user?id={b}) дуже сильно вдарив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')    
            
            if message.text == "кохатися" or message.text == 'Кохатися':
                await bot.send_message(message.chat.id, f"🥵❤️| [{nick_first_user}](tg://user?id={b}) жостко кохається з [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
        
            if message.text == "цьом" or message.text == 'Цьом':
                await bot.send_message(message.chat.id, f"💓🌸| [{nick_first_user}](tg://user?id={b}) поцьомав [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
                
            if message.text == 'дати підсрачника' or message.text == 'Дати підсрачника':
                await bot.send_message(message.chat.id, f"🦶☺️| [{nick_first_user}](tg://user?id={b}) дав підсрачника [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text == 'отруїти' or message.text == 'Отруїти':
                await bot.send_message(message.chat.id, f"🧪☠️| [{nick_first_user}](tg://user?id={b}) отруїв [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
            if message.text == 'покормити' or message.text == 'Покормити':
                await bot.send_message(message.chat.id, f"😋🍕| [{nick_first_user}](tg://user?id={b}) покормив [{nick_two_user}](tg://user?id={d})", parse_mode='Markdown')
            
    except TypeError:
        add_time = dtime.time(time.localtime())
        user_id = message.from_user.id
        username = message.from_user.username
        firstname = message.from_user.first_name
        if not db.check_id_bool(user_id):
            db.add_to_db(user_id, username, firstname, '')
            db.add_datetime(add_time, user_id)
        
        if db.check_nick(user_id) == None:
            db.nick_user(firstname, user_id)

            
        
    
        
if __name__ == '__main__':
    #запуск бота
    executor.start_polling(dp, skip_updates=True)
