# Name: Peter Kelt
# Date: 02-18-2013

def zellers(month, day, year):
    '''zellers_func.py - Zeller's algorithm computes the day of the week on
       which a given date will fall (or fell).
    '''
    days = {0 : 'Sunday',
            1 : 'Monday',
            2 : 'Tuesday',
            3 : 'Wedsday',
            4 : 'Thurdsay',
            5 : 'Friday',
            6 : 'Saturday',
            }
    months = {'Jan' : 1,
              'Feb' : 2,
              'Mar' : 3,
              'Apr' : 4,
              'May' : 5,
              'Jun' : 6,
              'Jul' : 7,
              'Aug' : 8,
              'Sep' : 9,
              'Oct' : 10,
              'Nov' : 11,
              'Dec' : 12,
              }

    # Assign variables to standard Zeller's algorithm terms.
    A = months[month]
    B = day
       
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

    print days[R]

zellers("Mar", 10, 1940)
zellers("Mar", 27, 1976)
zellers("Aug", 31, 1979)

