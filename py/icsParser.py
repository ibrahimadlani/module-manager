from ics import Calendar
import arrow
import json
import re

joursAJD = arrow.now('Europe/Paris').format('D')
moisAJD = arrow.now('Europe/Paris').format('m')
annéeAJD = arrow.now('Europe/Paris').format('YYYY')


with open('./input/edt.ics', 'r') as file:
    edt = file.read()


decalageUTC = 1
edt = Calendar(edt).events


def getDay(d, m, y):
    dayEvents = []
    for e in edt:
        if e.begin.day == d and e.begin.month == m and e.begin.year == y:
            dayEvents.append(e)
    return dayEvents

def getType(event):
    texte = event.description
    result = re.search('\)-(.*)\n', texte)

    if result is None:
        return ""
    else:
        return result.group(1)

def getProf(event):
    texte = event.description
    result = re.search('Prof : (.*)\n', texte)
    if result is None:
        return ""
    else:
        return result.group(1)

def getNom(event):
    texte = event.description
    result = re.search('-(.*)  \(', texte)
    if result is None:
        return ""
    else:
        return result.group(1)

def getModule(event):
    texte = event.description
    result = re.search(' \((.*)\)-', texte)
    
    if result is None:
        return ""
    else:
        module = result.group(1)[1]+result.group(1)[3]+"0"+result.group(1)[4]
        return module
    

def getDs(event):
    texte = event.description
    if("Commentaire" in texte):
        result = re.search('Commentaire : (.*)\n', texte)
        if result is None:
            return ""
        else:
            return result.group(1)
    else:
        return ""


def getMoodle(module):
    moodles = {
  "4101": "https://moodle.uphf.fr/course/view.php?id=1032",
  "4102": "",
  "4103": "https://moodle.uphf.fr/course/view.php?id=1359",
  "4104": "https://moodle.uphf.fr/course/view.php?id=1824",
  "4105": "https://moodle.uphf.fr/course/view.php?id=388",
  "4106": "https://moodle.uphf.fr/course/view.php?id=853",
  "4201": "https://moodle.uphf.fr/course/view.php?id=1049",
  "4202": "https://moodle.uphf.fr/course/view.php?id=1044",
  "4203": "https://moodle.uphf.fr/course/view.php?id=1614",
  "4204": "",
  "4205": "",
  "4206": "",
}
    if module == "":
        return ""
    else:
         return moodles[module]
   



def setDayJson(d, m, y):
    dayEvents = getDay(d, m, y)
    dayObject = []
    for i in dayEvents:

        event = {}
        event['type'] = getType(i)
        event['module'] = getModule(i)
        event['nom'] = getNom(i)
        event['prof'] = getProf(i)
        event['debut'] = str(i.begin.shift(hours=+1).format("H:mm:ss"))
        event['fin'] = str(i.end.shift(hours=+1).format("H:mm:ss"))
        event['duree'] = str(i.duration)
        event['exam'] = getDs(i)
        event['moodle'] = getMoodle(getModule(i))
        dayObject.append(event)
   
    with open('./data/'+str(d)+"-"+str(m)+"-"+str(y)+'.json', 'w') as outfile:
        json.dump(dayObject, outfile)


setDayJson(25, 2, 2021)
