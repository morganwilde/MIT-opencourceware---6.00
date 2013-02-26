Debugging
=========

### Floating points numbers on computers

#### Binary numbers

Our usual numbers are base ten. So an example would be  
`302 = 3*100 + 0*10 + 2*1`.

Binary is just `0` and `1`. Again a similar exampe, but in base two  
`(binary) 101 = (base 10) 1*2**2 + 0*2**1 + 1*2**0 = (base 10) 5`

Binary numbers take a lot more diggits to represent them than base 10. So to represent `n` digits, you will need `2**n` binary numbers.

Floating point numbers cause problems because we think in `base 10` and the pc in `base 2`. Computers work in `base 2`, because it is to build switches with two states.

Whole numbers - binary or decimal numbers don't have any difference, it's only float numbers that have issues.

A decimal point - `0.125 = 1/8 = 1*10**-1 + 2*10**-2 + 5*10**-3`

A binary point - `0.125 = 1/8 = 2**-3 = 1 * 10**-3 = (binary) 0.001`

*I found this tutorial on the IEEE standardized floating point storage formats*  
![IEEE floating point](http://kipirvine.com/asm/workbook/floating_tut.htm)

Decimal - `0.1 = 1*10**-1` and there is no finite way to display this decimal in binary.

**How Python really interprets decimals**

```Python
print(0.1*0.1)
# 0.01
repr(0.1*0.1)
# '0.010000000000000002'
```

Usually this doesn't matter. But there are cases where it does, as is the case in this example:

```Python
x = 0.0
numIters = 100000
for i in range(numIters):
    x += 0.1
print x #prints 10000.0, because print automatically rounds
# 10000.0
print repr(x)
# 10000.000000018848
print 10.0*x == numIters
```

If this worked like real numbers work, the end statement should produce `True`, but it doesn't.

The main takeaway is - do not test two floating point numbers if they are equal to each other. Instead use this technique:

```Python
def close(x, y, epsilon = 0.00001):
    return abs(x - y) <\ epsilon

if close(10.0*x, numIters):
    print 'Good enough'
```

### Debugging

#### Story

How the process of fixing flaws in programming came to be called debugging.

Computer scientists were running a program back in 1947.

![first slide](http://dl.dropbox.com/u/31042440/a-bug-1947.png)

After some four hours it stopped working.

![second slide](http://dl.dropbox.com/u/31042440/the-mark-II.png)

Once the search was complete, they found a moth caught between the relays.

![third slide](http://dl.dropbox.com/u/31042440/a-bug.png)

So they concluded that the program stopped working because of a bug. The first ever recorded occurence of a bug as writen in the book by Grace Murray.

![fourth slide](http://dl.dropbox.com/u/31042440/grace-murray-hopper.png)

#### Practical stuff

If there is a bug in your program - you put it there. It's a screw-up.

The goal of debugging is not to remove one bug quickly, it is to move toward a bug-free program.

Largest part of learning to be a good programmer is to learn how to systematically move towards a bug-free program. This still is also transferable.

#### Debuggers

Tools built to help us find bugs, but the tools are not that important, rather the skill of the craftsman. Print statements is almost always a better choice.

Key thing with searching out bugs using `print` statements is doint that systematically.

Search for bugs using binary search.

Questions to ask:

* How could it have done what it did?
* Study available data
    - program text
    - test results (adding `print` statements)
* Form a hypothesis consistent with the data
* Design & run a **repeatable** experiment
    - must have the potential to refute the hypothesis

Errors happen most commnly depending on:

* Randomness
* Timing issues
* User input

#### Examples

```Python
def silly(n):
    """requires: n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
    assert type(n) == int and n > 0
    for i in range(n):
        result= []
        elem = raw_input('Enter something: ')
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'

silly(3)
# Enter something: a
# Enter something: b
# Enter something: c
# Is a palindrome
```

The above example shows a function designed to check if the letter by letter input of a word is a palindrome. It has a bug, because when given `'abc'` it returns `'Is a palindrome'`, how to find this bug?

1. Find a smaller input that produces the same result

```Python
silly(1)
# Enter something: a
# Is a palindrome
```

This doesn't produce an error, increase the input to see the next case:

```Python
silly(2)
# Enter something: a
# Enter something: b
# Is a palindrome
```

This successfully replicates the bug. This is a good thing. Using binary search, we can devide the code in half and place a `print` statement somewhere around the middle.

```Python
def silly(n):
    """requires: n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
    assert type(n) == int and n > 0
    for i in range(n):
        result= []
        elem = raw_input('Enter something: ')
        print result # our first attempt to find a bug
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'
silly(2)
# Enter something: a
# []
# Enter something: b
# []
# Is a palindrome
```

So we found one issue - at the start of each `for` loops iteration, we reset `result = []`. So this doesn't carry over. After fixing this, we still don't get the desired outcome. So the leasson here is that there is never **the** bug, only **a** bug. This shows that the remaining bugs are below the `for` loop, in the function `isPal`, that is why next check is placed there.

Always when testing, write test code that allows for easy & fast testing - `test harness`. Like in this example:

```Python
def isPalTest():
    L = [1, 2]
    result = isPal(L)
    print 'Should print False:', result
    # Should print False: True
    L = [1, 2, 1]
    result = isPal(L)
    print 'Should print True:', result
    # Should print True: True
```

This is good, because it not only provides the outcome, but the expected outcome as well, this helps to scan the test results.
