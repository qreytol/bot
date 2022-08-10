from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DATETIME import date_time
import datetime

today = datetime.date.today()
one_day = today + datetime.timedelta(hours=3,days=1)
five_day = today + datetime.timedelta(hours=3,days=5)
two_day = today + datetime.timedelta(hours=3,days=2)
three_day = today + datetime.timedelta(hours=3,days=3)
four_day = today + datetime.timedelta(hours=3,days=4)
dtimee = date_time()
week_one = one_day.strftime('%A')
week_two = two_day.strftime('%A')
week_three = three_day.strftime('%A')
week_four = four_day.strftime('%A')
week_five = five_day.strftime('%A')

mainMenu = InlineKeyboardMarkup(row_width=3)

#ширина кнопок для команди Хто я
userKeyboard = InlineKeyboardMarkup(row_width=2)

#ширина кнопки добавити бота в свій чат
StartMenu = InlineKeyboardMarkup()


#значення кнопок з днями для погоди старт
oneBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_one)}', callback_data='one_weather')
threeBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_two)}', callback_data='two_weather')
thourBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_three)}', callback_data='three_weather')
fiveBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_four)}', callback_data='four_weather')
sixBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_five)}', callback_data='five_weather')
twoBTN = InlineKeyboardButton(text='Сьогодні', callback_data='today_weather')


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


#ініцілізація нопок з днями для погоди старт
mainMenu.insert(oneBTN)
mainMenu.insert(threeBTN)
mainMenu.insert(thourBTN)
mainMenu.insert(fiveBTN)
mainMenu.insert(sixBTN)
mainMenu.insert(twoBTN)

#кнопка назад
mainMenuNazad = InlineKeyboardMarkup()

NazadBTNS = InlineKeyboardButton(text='❌Назад', callback_data='Nazad_weather')
RestartBTNS = InlineKeyboardButton(text='➖Завершити', callback_data='Restart_weather')

mainMenuNazad.insert(NazadBTNS)
mainMenuNazad.insert(RestartBTNS)

MenuDetailOrShortOne = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_one')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_one')

MenuDetailOrShortOne.insert(Detail)
MenuDetailOrShortOne.insert(NazadBTNS)
MenuDetailOrShortOne.insert(Short)

MenuDetailOrShortTwo = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_two')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_two')

MenuDetailOrShortTwo.insert(Detail)
MenuDetailOrShortTwo.insert(NazadBTNS)
MenuDetailOrShortTwo.insert(Short)

MenuDetailOrShortThree = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_three')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_three')

MenuDetailOrShortThree.insert(Detail)
MenuDetailOrShortThree.insert(NazadBTNS)
MenuDetailOrShortThree.insert(Short)

MenuDetailOrShortFour = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_four')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_four')

MenuDetailOrShortFour.insert(Detail)
MenuDetailOrShortFour.insert(NazadBTNS)
MenuDetailOrShortFour.insert(Short)

MenuDetailOrShortFive = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_five')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_five')

MenuDetailOrShortFive.insert(Detail)
MenuDetailOrShortFive.insert(NazadBTNS)
MenuDetailOrShortFive.insert(Short)

MenuDetailOrShortToday = InlineKeyboardMarkup(row_width=3)

Detail = InlineKeyboardButton(text='📕більше', callback_data='Detail_weather_today')
Short = InlineKeyboardButton(text='📝менше', callback_data='Short_weather_today')

MenuDetailOrShortToday.insert(Detail)
MenuDetailOrShortToday.insert(NazadBTNS)
MenuDetailOrShortToday.insert(Short)
