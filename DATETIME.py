import datetime

class date_time():
    '''дата для БД'''
    def time(self):
        '''Підключення до часу'''
        self.todaytime = datetime.datetime.today().strftime("%m-%d-%Y %H:%M:%S")
        return (self.todaytime)
    
    def time_heroku(self):
        '''Підключення до часу HEROKY'''
        self.todaytime = datetime.datetime.today() + datetime.timedelta(hours=3)
        self.todaytime = self.todaytime.strftime("%m-%d-%Y %H:%M:%S")
        return (self.todaytime)
    
translate_days = {
    'Monday':'Понеділок',
    'Tuesday':'Вівторок',
    'Wednesday':'Середа',
    'Thursday':'Четвер',
    'Friday':'Пятниця',
    'Saturday':'Субота',
    'Sunday':'Неділя'
}
