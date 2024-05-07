import datetime


class Date:

    def __init__(self, input_date: str):
        if input_date[2] != '.' or input_date[5] != '.':
            self.__date = None
        else:
            try:
                input_obj = input_date + ' 00:00:00'
                datetime.datetime.strptime(input_obj, '%d.%m.%Y %H:%M:%S')
                self.__date = input_date
            except:
                self.__date = None

    def __repr__(self):
        if self.__date is None:
            return None
        return f'Date({self.__date[0:2]}, {self.__date[3:5]}, {self.__date[6:]})'

    def __str__(self):
        return f'{self.date}'

    def __lt__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self < date_other

    def __le__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self <= date_other

    def __eq__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self == date_other

    def __ne__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self != date_other

    def __ge__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self >= date_other

    def __gt__(self, other):
        day_self, day_other = int(self.__date[0:2]), int(other.__date[0:2])
        month_self, month_other = int(self.__date[3:5]), int(other.__date[3:5])
        year_self, year_other = int(self.__date[6:]), int(other.__date[6:])

        date_self = datetime.date(year_self, month_self, day_self)
        date_other = datetime.date(year_other, month_other, day_other)
        return date_self > date_other

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date: str):
        if new_date[2] != '.' or new_date[5] != '.':
            self.__date = None
        else:
            try:
                input_obj = new_date + ' 00:00:00'
                datetime.datetime.strptime(input_obj, '%d.%m.%Y %H:%M:%S')
                self.__date = new_date
            except:
                self.__date = None

    @date.getter
    def date(self):
        date_format = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл', 8: 'авг', 9: 'сен',
                       10: 'окт', 11: 'ноя', 12: 'дек'}
        if self.__date is not None:
            return f'{int(self.__date[0:2])} {date_format[int(self.__date[3:5])]} {self.__date[6:]} г.'
        else:
            print('ошибка')

    def to_timestamp(self):
        if self.__date is not None:
            day = int(self.__date[0:2])
            month = int(self.__date[3:5])
            year = int(self.__date[6:])

            our_date = datetime.date(year, month, day)
            start_date = datetime.date(year=1970, month=1, day=1)
            delta = our_date - start_date
            return int(delta.total_seconds())
