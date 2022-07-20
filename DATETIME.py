import time
from translate import Translator

class date_time():
    '''дата для БД'''
    def time(self, user_data):
        '''Підключення до часу'''
        self.todaytime = time.strftime("%m-%d-%Y %H:%M:%S", user_data)
        return (self.todaytime)
    
    def transweek(self, week):
        '''Переклад тексту для РП команди ДАТА WEEK'''
        tran = Translator(from_lang='english', to_lang='uk')
        translate_week = tran.translate(week)
        return (translate_week)
    
    def transmonth(self, month):
        '''Переклад тексту для РП команди ДАТА MONTH'''
        tran = Translator(from_lang='english', to_lang='uk')
        translate_month = tran.translate(month)
        return (translate_month)

