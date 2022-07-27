from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DATETIME import date_time
import datetime

today = datetime.date.today()
six_day = today + datetime.timedelta(hours=3,days=5)
two_day = today + datetime.timedelta(hours=3,days=1)
three_day = today + datetime.timedelta(hours=3,days=2)
thour_day = today + datetime.timedelta(hours=3,days=3)
five_day = today + datetime.timedelta(hours=3,days=4)
dtimee = date_time()

week_two = two_day.strftime('%A')
week_three = three_day.strftime('%A')
week_thour = thour_day.strftime('%A')
week_five = five_day.strftime('%A')
week_six = six_day.strftime('%A')

mainMenuNazad = InlineKeyboardMarkup()

mainMenuThree = InlineKeyboardMarkup(row_width=3)

mainMenuTwo = InlineKeyboardMarkup(row_width=3)

#ширина кнопок для з днями для погоди 1
mainMenuOne = InlineKeyboardMarkup(row_width=3)

#ширина кнопок для команди Хто я
userKeyboard = InlineKeyboardMarkup(row_width=2)

#ширина кнопки добавити бота в свій чат
StartMenu = InlineKeyboardMarkup()


oneBTNT = InlineKeyboardButton(text='Деталі', callback_data='detaliTwo')
threeBTNT = InlineKeyboardButton(text=f'{dtimee.transweek(week_three)}', callback_data='left_weather')
thourBTNT = InlineKeyboardButton(text=f'{dtimee.transweek(week_thour)}', callback_data='thourbtn')
fiveBTNT = InlineKeyboardButton(text=f'{dtimee.transweek(week_five)}', callback_data='fivebtn')
sixBTNT = InlineKeyboardButton(text=f'{dtimee.transweek(week_six)}', callback_data='sixbtn')
twoBTNT = InlineKeyboardButton(text='Сьогодні', callback_data='twobtn')


#значення кнопок з днями для погоди 1
oneBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_two)}', callback_data='right_weather')
threeBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_three)}', callback_data='left_weather')
thourBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_thour)}', callback_data='thourbtn')
fiveBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_five)}', callback_data='fivebtn')
sixBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_six)}', callback_data='sixbtn')
twoBTN = InlineKeyboardButton(text='Деталі', callback_data='detaliOne')


#значення кнопок з днями для погоди старт
oneBTNS = InlineKeyboardButton(text=f'{dtimee.transweek(week_two)}', callback_data='right_weather')
threeBTNS = InlineKeyboardButton(text=f'{dtimee.transweek(week_three)}', callback_data='left_weather')
thourBTNS = InlineKeyboardButton(text=f'{dtimee.transweek(week_thour)}', callback_data='thourbtn')
fiveBTNS = InlineKeyboardButton(text=f'{dtimee.transweek(week_five)}', callback_data='fivebtn')
sixBTNS = InlineKeyboardButton(text=f'{dtimee.transweek(week_six)}', callback_data='sixbtn')
twoBTNS = InlineKeyboardButton(text='Сьогодні', callback_data='twobtn')



NazadBTN = InlineKeyboardButton(text='Назад!', callback_data='Nazad')


#значення кнопки для добавити бота в чат
startBTN = InlineKeyboardButton(text='Добавити', url='https://telegram.me/Arnold_new_chat_bot?startgroup=new')

#значення кнопки для Хто я
opisBTN = InlineKeyboardButton(text='📕Опис', callback_data='getOpis')
statusBTN = InlineKeyboardButton(text='😊Що я вмію', callback_data='getCommands')

#ініцілізація кнопок для команди Хто я
userKeyboard.insert(opisBTN)
userKeyboard.insert(statusBTN)

#ініцілізація добавити бота в свій чат
StartMenu.insert(startBTN)

#ініцілізація кнопок з днями для погоди 1
mainMenuOne.insert(oneBTN)
mainMenuOne.insert(threeBTN)
mainMenuOne.insert(thourBTN)
mainMenuOne.insert(fiveBTN)
mainMenuOne.insert(sixBTN)
mainMenuOne.insert(twoBTN)

#ініцілізація нопок з днями для погоди старт
mainMenuTwo.insert(oneBTNS)
mainMenuTwo.insert(threeBTNS)
mainMenuTwo.insert(thourBTNS)
mainMenuTwo.insert(fiveBTNS)
mainMenuTwo.insert(sixBTNS)
mainMenuTwo.insert(twoBTNS)


mainMenuNazad.insert(NazadBTN)

mainMenuThree.insert(oneBTNT)
mainMenuThree.insert(threeBTNT)
mainMenuThree.insert(thourBTNT)
mainMenuThree.insert(fiveBTNT)
mainMenuThree.insert(sixBTNT)
mainMenuThree.insert(twoBTNT)



