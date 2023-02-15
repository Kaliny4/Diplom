"""
Написать программу для работы с данными о людях.
Программа должна уметь загружать данные из файла, сохранять в файл,
вводить новые записи и производить поиск по существующим записям.

Программа сохраняет данные о человеке, а именно:
ФИО, дата рождения, дата смерти (может отсутствовать) и пол.
При этом ФИО вводится 3 полями: Имя (обязательно), Фамилия и Отчество могут не вводится.

Программа должна уметь вычислять возраст человека (количество полных лет)
на основании даты рождения и даты смерти или сегодняшней даты, если дата смерти отсутствует.
Дата рождения и дата смерти может вводится в формате:
12.10.1980
11 10 2000
01/02/1995
3-9-2007
Поиск может производится по имени, фамилии и отчеству и выдаёт все варианты,
которые подходят под строку поиска (это может быть имя, или фамилия, или имя и фамилия,
или только часть имени и т.д.).
К примеру, есть такие записи:
Евгений Крут Михайлович, 12.10.1980, 11.10.2001, m
Евгения, 12.10.1980, 12.10.2001, f
Дмитрий Евгеньевич, 10.03.2000, m

При поиске "евген", выдаются такие данные:
Евгений Крут Михайлович  20 лет, мужчина. Родился: 12.10.1980. Умер: 11.10.2001.
Евгения 21 год, женщина. Родилась: 12.10.1980. Умерла: 12.10.2001.
Дмитрий Евгеньевич 22 года, мужчина. Родился: 10.03.2000.

Программа при старте начинает работать с пустой базой данных.
Оператор может заполнять её,
а может при желании загрузить ранее сохранённые данные из файла (желательно Excel).
Когда есть какие-то записи оператор может сохранить их в файл введя его название.

Желательная структура программы:
в основной части программы находится вечный цикл с меню, что может выбрать оператор;
сами данные организованы в виде класса в другом файле,
который импортируется в файл основной части программы,
где создаётся объект соответствующего класса перед заходом в вечный цикл;
все пункты меню основной части программы вызывают те или иные методы у созданного объекта данных;
при желании можно в третьем файле создать отдельный класс Person
который будет импортироваться в файл с данными.
Именно в этом классе будет происходить валидация введённых данных.

*Все перечисленные описания являются пожеланиями по реализации дипломного проекта
и в силу тех или иных причин могут быть изменены по желанию студента.
Основные требования:
программа позволяет ввести новые данные о людях;
производить поиск по уже введённым данным;
правильно рассчитывать количество полных лет человека на основе даты рождения
и даты смерти или текущей даты.

"""

import csv
from Person import Person
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta


def fist_time():
    person = Person(input('Pls, enter the name (necessary field): ')
                    , input('the date of birth dd.mm.yyyy (necessary field): ')
                    , input('the gender (necessary field): ')
                    , input('the date of death if any dd.mm.yyyy : ')
                    , input('the surname if any: ')
                    , input('the father name if any: ')
                    )
    person_lst = [person.name, person.surname, person.father_name
        , person.birth_date, person.death_date, person.gender]
    colum_names = ['name', 'surname', 'father name', 'birth', 'death', 'gender']

    with open('person_csv.csv', mode='w', encoding='utf-8', newline='') as f:
        file_writer = csv.writer(f)
        file_writer.writerow(colum_names)
        file_writer.writerow(person_lst)

#fist_time() #ця функція викликається тільки перший раз щоб створити файл


def search():
    while True:
        perform_cycle1 = input('Do you want to search? (Y/N): ')
        if perform_cycle1.upper() in 'Y':
            parameter = input('Enter name, surname or father name: ')
            with open('person_csv.csv', mode='r') as f:
                reader = csv.reader(f)
                for item, row in enumerate(reader):
                    for item in row:
                        if parameter.capitalize() in item:
                            print(row)
                            perform_cycle2 = input('Do you want to count age? (Y/N): ')
                            if perform_cycle2.upper() in 'Y':
                                a = row[3].replace(' ', '/').replace('.', '/') \
                                    .replace('-', '/')
                                born = datetime.strptime(a, '%d/%m/%Y')
                                # death or no death
                                b = row[4].replace(' ', '/').replace('.', '/') \
                                    .replace('-', '/')
                                if b != '':
                                    fin_d = datetime.strptime(b, '%d/%m/%Y')
                                else:
                                    fin_d = date.today()
                                # age
                                age = relativedelta(fin_d, born)
                                print(age.years)
                                second_time()
                                break
                            else:
                                second_time()
                                break
        else:
            break

        break


def second_time():
    while True:
        perform_cycle = input('Do you want to add more? (Y/N): ')
        if perform_cycle.upper() in 'Y':
            person = Person(input('Pls, enter the name (necessary field): ')
                            , input('the date of birth dd.mm.yyyy (necessary field): ')
                            , input('the gender (necessary field): ')
                            , input('the date of death if any dd.mm.yyyy : ')
                            , input('the surname if any: ')
                            , input('the father name if any: ')
                            )
            person_lst = [person.name, person.surname, person.father_name
                , person.birth_date, person.death_date, person.gender]
            with open('person_csv.csv', mode='a') as f:
                file_writer = csv.writer(f)
                file_writer.writerow(person_lst)
                continue
        else:
            search()
        break


second_time()




