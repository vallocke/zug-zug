# Name: Peter Kelt
# Date: 01-20-2013
# rps.py - Rock, Paper, Scissors game.

r = 'rock'
p = 'paper'
s = 'scissors'

while True:
    p1 = raw_input('Player 1? ')
    if p1 == r or p1 == p or p1 == s:
        p2 = raw_input('Player 2? ')
        if p2 == r or p2 == p or p2 == s:
            if p1 == r and p2 == r:
                print 'Player 1 and Player 2 tie.'
            elif p1 == r and p2 == p:
                print 'Player 2 wins.'
            elif p1 == r and p2 == s:
                print 'Player 1 wins.'
            elif p1 == p and p2 == r:
                print 'Player 1 wins.'
            elif p1 == p and p2 == p:
                print 'Player 1 and Player 2 tie.'
            elif p1 == p and p2 == s:
                print 'Player 2 wins.'
            elif p1 == s and p2 == r:
                print 'Player 2 wins.'
            elif p1 == s and p2 == p:
                print 'Player 1 wins.'
            elif p1 == s and p2 == s:
                print 'Player 1 and Player 2 tie.'
        else:
            print 'This is not a valid object selection.'
    else:
        print 'This is not a valid object selection.'
