# Name: Peter Kelt
# Date: 01-20-2013
# loops.py - Various loops exercises.

### Exercise 1
##for nums in range(2, 11):
##    print 1.0 / nums

### Exercise 2
##num = input('Enter a number: ')
##if num > 0:  
##    while num > 0:
##        print num
##        num -= 1
##else:
##    print 'Please enter an integer greater than zero.'

# Exercise 3
# ???

# Exercise 4
num = input('Enter a # divisible by 2: ')
if num % 2 != 0: 
    while num % 2 != 0:
        print 'Flesh wound to the skull? %d is not divisible by 2.' % num
        num = input('Enter a new #: ')
    print 'Congratz %d is divisible by 2...Took you long enough champ' % num
else:
    print 'Yep, that # is divisible by 2'
