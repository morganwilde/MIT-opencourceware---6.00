###
### Recitation 2 Code
###

###
### What is the decrementing function?
### What does this loop do?
###

### Print even numbers from 2 to 10
##a = 2
##while a <= 10:
##    a += 2
##    print a

###
### For loop
###
### For loops require something that is enumerable, I.e. for loops iterate over an enumerable item
##for i in (2,4,6,8,10):
##    print i
##
### Kind of inconvenient.

###
### Range function
###
##print range(100) # the start is 0
##print range(1, 100) # first parameter inclusive, the second one exclusive
##print range(1, 100, 2)
##print range(100, 1, -1)

##for i in range(2, 1001, 2):
##    print  i

###
### Tuple
###
### homogenous data structure, I.e. only type `int` or type `str`
##tuple_of_numbers = (3.14159, 2, 1, -100, 100, 240)
##tuple_of_strings = ('What', 'is', 'my', 'name?')

### Tuples start at index 0
##print tuple_of_numbers[0]
##print tuple_of_strings[0]
##print tuple_of_strings[-1]
##print tuple_of_strings[4] # IndexError: tuple index out of range

### how many elements in the tupl
##print len(tuple_of_numbers)

### can hold different types - heterogenous data structure
##tuple_of_numbers_and_strings = (3.14159, 'is', 'an imperfect', 'representation')
##
### including other tuples
##tuple_of_tuples = (('stuff', 'just'), 'got', 'real')
##print tuple_of_tuples[0]

### Can't do this! Tuples are immutable
##tuple_of_numbers[0] = 3

### slice (but not dice)
##print tuple_of_numbers[1:3]
##print tuple_of_numbers[:2]
##print tuple_of_numbers[1:]
##print tuple_of_numbers[:-1]

### iterate over
##for number in tuple_of_numbers:
##    print number
##
###
### Oddity
###
##print 'Before:', tuple_of_numbers
##tuple_of_numbers = tuple_of_numbers + (100,20)
##print 'After:', tuple_of_numbers

###
### Wart.
###
##oopsie = (50)  # creates an int object
##print 'oopsie:', oopsie
##onsie = (50,)
##print 'onsie:', onsie

###
### Strings
###
##name = 'Mitch'
##
##print name
##print name[0]
##print name[1]
###name[0] = 'P' # Wrong!
### iterate over a string
##for letter in name:
##    print letter
##
###print name[1:3]
##
### functions
##print name.upper()
##print name.lower()
##print name.find('i')
##print name.replace('M', 'P')
##print name.lower().replace('m', 'p')

###
### Example of using break
###
##x = int(raw_input('Enter an integer:'))
##ans = 0
##while ans**3 < abs(x):
##    ans += 1
##    print 'current guess =', ans
##
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)

##x = int(raw_input('Enter an integer:'))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)

###
### Functions
###
##def cube(number):
##    """Takes a number and returns the cube of that number.
##    Input: number (float or int)
##    Output: number (float)"""
##    return number**3
##
##print cube(3)
##print cube(5)
##
##def times2(number):
##    """Takes a number and doubles it
##    Input: number (float or int)
##    Output: number (float)"""
##    return number*2

###
### Variable scope
###
##all_hope = "Here be dragons"
##def all_your_vars_are_belong_to_us(variables):
##    """Steals all your variables.
##    Input: variables (stuff)
##    Output: None (it's stolen)
##    """
##    my_variable = 'Make your time'
##    print "parameter passed into the function:", variables
##    print "Global variable:", all_hope
##    print "Local variable:", my_variable
##
##old_meme_is_old = 'Somebody set up us the bomb'
##all_your_vars_are_belong_to_us(old_meme_is_old)
##
###
### What happens here?
###
##print my_variable # returns an error, it's not defined, because it's defined within a functions scope

##global_int = 0
##def incIt(x):
##    global global_int
##    x += 1
##    global_int += 1
##    return x
##
##y = 10
##print incIt(y)
##print global_int
##print y

#
# Print is not return
#
def print_is_not_return():
    print 'This will return none'
def return_is_not_print():
    return 'This will return a string'

print print_is_not_return()
print return_is_not_print()

#
# Functions are objects, be vary of the parentheses
#

print return_is_not_print
# <function return_is_not_print at 0x3311ed8>
