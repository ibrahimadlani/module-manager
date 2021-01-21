from ics import Calendar

with open('./input/edt.ics', 'r') as file:
    edt = file.read()


c = Calendar(edt)
decalageUTC = 0

print(c.events[30].name)