from ics import Calendar
import arrow
import json


with open('./input/edt.ics', 'r') as file:
    edt = file.read()


decalageUTC = 2
edt = Calendar(edt).events


def getDay(d, m, y):
    dayEvents = []
    for e in edt:
        if e.begin.day == d and e.begin.month == m and e.begin.year == y:
            dayEvents.append(e)
    return dayEvents




def setDayJson(d, m, y):
    dayEvents = getDay(d, m, y)
    dayObject = []
    for i in dayEvents:
        event = {}
        event['people'] = []
        event['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        event['people'].append({
            'name': 'Larry',
            'website': 'google.com',
            'from': 'Michigan'
        })
        event['people'].append({
            'name': 'Tim',
            'website': 'apple.com',
            'from': 'Alabama'
        })
        dayObject.append(event)
    
   
    with open('./data/'+str(d)+"-"+str(m)+"-"+str(y)+'.json', 'w') as outfile:
        json.dump(dayObject, outfile)


setDayJson(11, 2, 2021)




utc = arrow.utcnow().to('Europe/Paris')
print(utc)