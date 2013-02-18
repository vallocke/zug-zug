# Name: Pete Kelt
# Section: 1337
# hw2.py - 01/27/2013

import math
import random

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

##def f1(x):
##    print x + 1
##
##def f2(x):
##    return x + 1

### **********  Exercise 2.1 ********** 
##
### Define your function here
### Functionized version of rock, paper scissors
##
##def rps(p1, p2):
##    r = 'rock'
##    p = 'paper'
##    s = 'scissors'
##    if p1 == r or p1 == p or p1 == s:
##        if p2 == r or p2 == p or p2 == s:
##            if p1 == r and p2 == r:
##                return 'Player 1 and Player 2 tie.'
##            elif p1 == r and p2 == p:
##                return 'Player 2 wins.'
##            elif p1 == r and p2 == s:
##                return 'Player 1 wins.'
##            elif p1 == p and p2 == r:
##                return 'Player 1 wins.'
##            elif p1 == p and p2 == p:
##                return 'Player 1 and Player 2 tie.'
##            elif p1 == p and p2 == s:
##                return 'Player 2 wins.'
##            elif p1 == s and p2 == r:
##                return 'Player 2 wins.'
##            elif p1 == s and p2 == p:
##                return 'Player 1 wins.'
##            elif p1 == s and p2 == s:
##                return 'Player 1 and Player 2 tie.'
##        else:
##            return 'This is not a valid object selection.'
##    else:
##        return 'This is not a valid object selection.'
##
### Test Cases for Exercise 2.1
### Test 1
##print rps('paper', 'rock')
##
### Test 2
##print rps('scissors', 'rock')
##
### Test 3
##print rps('paper', 'cow')

### ********** Exercise 2.2 ********** 
##
### Define is_divisible function here
##def is_divisible(m, n):
##    if n != 0:
##        if m % n == 0 and n != 0:
##            return True
##        elif n != 0:
##            return False
##    else:
##        return 'Divide by 0, please choose alternate denominator.'
##
### Test cases for is_divisible
#### Provided for you... uncomment when you're done defining your function
##
##print is_divisible(10, 5)  # This should return True
##print is_divisible(18, 7)  # This should return False
##print is_divisible(42, 0)  # What should this return?


### Define not_equal function here
##def not_equal(val1, val2):
##    if val1 == val2:
##        return False
##    else:
##        return True
##
### Test cases for not_equal
### Test 1
##print not_equal(6, 8)
##print 6 != 8
##
### Test 2
##print not_equal('cake', 11.0)
##print 'cake' != 11.0
##
### Test 1
##print not_equal('dog', 'dog')
##print 'dog' != 'dog'

### ********** Exercise 2.3 ********** 
##
#### 1 - multadd function
##def multadd(a, b, c):
##    return a*b + c
##
##ceiling_test = multadd(2, math.log(12, 7), math.ceil(276/19.0))
##print "ceiling(276/19) + 2 log_7(12) is:"
##print ceiling_test
##
##angle_test = multadd(0.5, math.cos(math.pi/4), math.sin(math.pi/4))
##print "sin(pi/4) + cos(pi/4)/2 is:"
##print angle_test
##
#### 3 - yikes function
##def yikes(x):
##    return multadd(x, math.e**(-x), math.sqrt(1 - math.e**(-x)))
##
##
### Test Cases
##x = 5
##print "yikes(5) =", yikes(x)

### ********** Exercise 2.4 **********
##
#### 1 - rand_divis_3 function
##def rand_divis_3():
##    num = random.randint(0, 100)
##    print num
##    if num % 3 == 0:
##        return True
##    else:
##        return False
##
### Test Cases
##print rand_divis_3()
##print rand_divis_3()
##print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##def roll_dice(sides, times):
##    for i in range(0, times):
##        print random.randint(1, sides)
##        i += 1
##    return "That's all!"
##
### Test Cases
##print roll_dice(6, 3)
##print roll_dice(20, 1)
##print roll_dice(10, 5)

# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
    # Calculate discrim to determine if root is complex.
    d = b**2 - 4*a*c
    if d > 0:   # Two roots
        root1 = ((-b) + math.sqrt(d))/2*a
        root2 = ((-b) - math.sqrt(d))/2*a
        return root1, root2
    elif d == 0: # double root
        droot = -1 * (b/2*a)
        return droot
    else:
        return "Error! Roots are complex, Oh noes!"

# Test Cases
# real roots
print roots(1, 10, 1)

# double root
print roots(1, 2, 1)

# complex root
print roots(10, 2, 10)
##### YOUR CODE HERE #####   
