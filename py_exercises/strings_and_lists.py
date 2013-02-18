# Name:
# Section:
# strings_and_lists.py

### **********  Exercise 2.7 **********
##
##def sum_all(number_list):
##    # number_list is a list of numbers
##    total = 0
##    for num in number_list:
##        total += num
##
##    return total
### Test cases
##print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
##print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])
##
##def cumulative_sum(number_list):
##    # number_list is a list of numbers
##    c_sum = 0
##    total_list = []
##    for n in number_list:
##        c_sum += n
##        total_list.append(c_sum)
##    return total_list
### Test Cases
##print cumulative_sum([4, 3, 6])


### **********  Exercise 2.8 **********
##
##def report_card():
##    gpa = 0.0
##    card = {}
##    num_class = int(raw_input("How many classes did you take? "))
##    for i in range(num_class):
##        class_name = raw_input("What was the name of this class? ")
##        class_grade = int(raw_input("What was your grade? "))
##        card[class_name] = class_grade
##
##    print "Report Card:"
##    for key in card:
##        gpa += card[key]
##        print key, "-", card[key]
##    print "Overall GPA", gpa / num_class
##    
##
##report_card()
# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

##VOWELS = ['a', 'e', 'i', 'o', 'u']
##
##def pig_latin(word):
##    # word is a string to convert to pig-latin
##    if VOWELS.count(word[0]) == 0:
##        return word[1:] + word[0] + 'ay'
##    else:
##        return word + 'ay'
##
### Test Cases
##print pig_latin('pear')
##print pig_latin('apple')


### **********  Exercise 2.10 **********
##cubes = [ x ** 3 for x in range(1, 11)]
##print cubes

##two_flips = [i+j for i in ['h', 't'] for j in ['h', 't']]
##print two_flips

##string = 'mississippi'
##VOWELS = ['a', 'e', 'i', 'o', 'u']
##
##all_vowels = [i for i in string if VOWELS.count(i) == 1]
##print all_vowels
##
### Non list comprehension version of above
##all_vowels = []
##for i in string:
##    if VOWELS.count(i) == 1:
##        all_vowels.append(i)
##print all_vowels





### Test Cases
####### YOUR CODE HERE #####


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
