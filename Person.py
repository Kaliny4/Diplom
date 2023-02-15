from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


class Person(object):
    name = None
    surname = None
    father_name = None
    birth_date = '11/11/1111'
    death_date = '11/11/1111'
    gender = None

    def __init__(self, name, birth_date, gender, death_date=''
                 , surname='', father_name=''):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.death_date = death_date
        self.gender = gender
        self.birth_date = birth_date

    def age(self):
        #birth
        a = self.birth_date.replace(' ', '/').replace('.', '/') \
            .replace('-', '/')
        born = datetime.strptime(a, '%d/%m/%Y')
        #death or no death
        b = self.death_date.replace(' ', '/').replace('.', '/') \
            .replace('-', '/')
        if b != '':
            fin_d = datetime.strptime(b, '%d/%m/%Y')
        else:
            fin_d = date.today()
        #age
        age = relativedelta(fin_d, born)
        return age.years


