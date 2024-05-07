class AirTicket:
    passenger_name = []
    _from = []
    to = []
    date_time = []
    flight = []
    seat = []
    _class = []
    gate = []

    def __init__(self, info: list):
        self.__info = info
        self.__pname, self.__frm, self.__to, self.__dt, self.__fl, self.__st, self.__cl, self.__gt = info
        AirTicket.passenger_name.append(self.__pname)
        AirTicket._from.append(self.__frm)
        AirTicket.to.append(self.__to)
        AirTicket.date_time.append(self.__dt)
        AirTicket.flight.append(self.__fl)
        AirTicket.seat.append(self.__st)
        AirTicket._class.append(self.__cl)
        AirTicket.gate.append(self.__gt)

    def __repr__(self):
        return f'AirTicket({self.__info})'

    def __str__(self):
        return (f'|{self.__pname}{" " * (16 - len(self.__pname))}|{self.__frm} |{self.__to}|{self.__dt}|{self.__fl}'
                f'{" " * (20 - len(self.__fl))}|{self.__st}{" " * (4 - len(self.__st))}|{self.__cl}  |{self.__gt}'
                f'{" " * (4 - len(self.__gt))}|')


class Load:
    data = []

    @classmethod
    def write(cls, file):
        with open(file, encoding='utf-8') as f:
            f_to_list = f.read().split('\n')
            for row in f_to_list[1:]:
                row = row[:-1]
                row = row.split(';')
                ticket = AirTicket(row)
                Load.data.append(ticket)
        return f_to_list
