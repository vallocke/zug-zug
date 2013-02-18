# Name: Peter Kelt
# Date: 01-20-2013
# zellers.py - Zeller's algorithm computes the day of the week on which a
#              given date will fall (or fell).

A = int(raw_input('Enter Month (MM): '))
B = input('Enter Day (DD): ')
year = input('Enter Year (YYYY): ')

# Format month so March = 1...February = 12, decriment year if Jan or Feb.
if A == 1 or A == 2:
    A += 10
    year -= 1
else:
    A -= 2

C = year % 100
D = (year - C) / 100
W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z % 7

# Fix 'R' if negative.
if R < 0:
    R += 7

days = {0 : 'Sunday',
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wedsday',
        4 : 'Thurdsay',
        5 : 'Friday',
        6 : 'Saturday',
        }

print days[R]



