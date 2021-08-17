import time, datetime

def Get_fecha(dia=0):

    if dia == 1:
        Date = datetime.datetime.now()
        Date = Date.date()
        return Date
    else:
        Hours = datetime.datetime.now().strftime('%H:%M:%S')
        Date = datetime.datetime.now().strftime('%Y-%m-%d')
        fecha_peso = Date + " " + Hours
        return fecha_peso