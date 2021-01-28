from ics import Calendar

with open('./input/edt.ics', 'r') as file:
    edt = file.read()


decalageUTC = 2
edt = Calendar(edt).events

def getDay(d,m,y):
    dayEvents = []
    for e in edt:
        if e.begin.day == d and e.begin.month == m and e.begin.year == y :
            dayEvents.append(e)
    return dayEvents

    