from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DATETIME import date_time
import datetime

today = datetime.date.today()
six_day = today + datetime.timedelta(days=4)
two_day = today + datetime.timedelta(days=0)
three_day = today + datetime.timedelta(days=1)
thour_day = today + datetime.timedelta(days=2)
five_day = today + datetime.timedelta(days=3)
dtimee = date_time()

week_two = two_day.strftime('%A')
week_three = three_day.strftime('%A')
week_thour = thour_day.strftime('%A')
week_five = five_day.strftime('%A')
week_six = six_day.strftime('%A')
mainMenu = InlineKeyboardMarkup(row_width=3)
oneBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_two)}', callback_data='right_weather')
threeBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_three)}', callback_data='left_weather')
thourBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_thour)}', callback_data='thourbtn')
fiveBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_five)}', callback_data='fivebtn')
sixBTN = InlineKeyboardButton(text=f'{dtimee.transweek(week_six)}', callback_data='sixbtn')
twoBTN = InlineKeyboardButton(text='Сьогодні', callback_data='twobtn')

mainMenu.insert(oneBTN)
mainMenu.insert(threeBTN)
mainMenu.insert(thourBTN)
mainMenu.insert(fiveBTN)
mainMenu.insert(sixBTN)
mainMenu.insert(twoBTN)
