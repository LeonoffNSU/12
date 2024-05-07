import numpy as np
from m_task1 import Date


class Meeting:
    lst_meeting = []

    def __init__(self, info: list):
        self.id = info[0][0]
        self.date = info[0][1]
        self.title = info[0][2]

        employees = info[1]
        self.employees = employees[0]
        if len(employees) > 1:
            for person in employees[1:]:
                self.employees = np.vstack([self.employees, person])

        Meeting.lst_meeting.append(self)

    def __str__(self):
        text = f'Рабочая встреча {self.id}\n{self.date} {self.title}\n'
        for row in self.employees:
            full_name = row[3] + ' ' + row[2] + ' ' + row[4]
            full_name = full_name.strip()
            if row[5] != '':
                text += f'ID: {row[0]} LOGIN: {row[1]} NAME: {full_name} GENDER: {row[5]}\n'
            else:
                text += f'ID: {row[0]} LOGIN: {row[1]} NAME: {full_name}\n'
        return text

    def add_person(self, person: list):
        person = np.array(person)
        self.employees = np.vstack([self.employees, person])

    def count(self):
        return len(self.employees)

    @classmethod
    def count_meeting(cls, date: Date):
        cnt = 0
        for self in cls.lst_meeting:
            meeting_date = Date(self.date)
            if str(meeting_date) == str(date.date):
                cnt += 1
        return cnt

    @classmethod
    def total(cls):
        cnt = 0
        for self in cls.lst_meeting:
            cnt += len(self.employees)
        return cnt


class Load:

    @classmethod
    def write(cls, f_meetings: str, f_persons: str, f_pers_meetings: str):
        meetings = np.loadtxt(f_meetings, dtype=np.str_, delimiter=';', encoding='utf-8')
        meetings = meetings[:, :3]
        persons = np.loadtxt(f_persons, dtype=np.str_, delimiter=';', encoding='utf-8')
        persons = persons[:, :6]
        pers_meetings = np.loadtxt(f_pers_meetings, dtype=np.str_, delimiter=';', encoding='utf-8')
        pers_meetings = pers_meetings[:, :2]

        for id_meet in meetings[1:, 0]:
            id_people_present = pers_meetings[pers_meetings[:, 0] == id_meet][:, 1]
            people_present = []
            for id_people in id_people_present:
                pers_slice = persons[int(id_people)]
                people_present.append(pers_slice)

            info = [meetings[int(id_meet)], people_present]
            meet = Meeting(info)
