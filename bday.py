from datetime import date

d0 = date(2001, 2, 14)
d1 = date(2018, 2, 14)

delta = d1 - d0

minus = (delta.days/365)

bday = ("Happy %s Birthday!") %minus

print(bday)
