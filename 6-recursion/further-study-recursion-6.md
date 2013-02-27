Conditionals and recursion
==========================

### The modulues operator

The **modulues operator** - `%`, works on integers and yields the remainder after diving 1st operand by the 2nd.

```Python
quotient = 7 / 3
print quotient
# 2
remainder = 7 % 3
print remainder
# 1
```

Modules is useful when:

1. Checking if `2` numbers are even divisble by each other
2. Extracting right-most digits, I.e. `567 % 10 = 7` and `567 % 100 = 67`

### Boolean expressions

A **boolean expression** is either `True` or `False`. An example of a `boolean` expressions:

```Python
print 5 == 5
# True
print 5 == 6
# False
```

Besides `==` there are other **comparison operators** that produce a `boolean`:

* `x != y` - x is not equal to y
* `x > y`  - x is greater than y
* `x < y`  - x is less than y
* `x >= y` - x is greater than or equal to y
* `x <= y` - x is less than or equal to y

### Logical operators

There are three **logical operators**:

* `and` - returns `True` if both boolean expressions are `True`
* `or` - returns `True` if both or any one of the boolean expressions are `True`
* `not` - negates boolean expression: `True` -> `False` and `False` -> `True`

Operands of these operators should be `boolean` expressions, but Python will interpret any `nonzero` number as `True`.

### Conditional execution

```Python
if x > 0:
    print 'x is positive'
```

`if` allows for a **conditional statement**, what follows it `x > 0` is the **condition**. If the condition evaluates `True`, then the if's block of statements is executed.

`pass` - a good placeholder for an `if` block of statements when it isn't writen yet.

### Alternative execution

```Python
if x%2 == 0: 
    print x, "is even" 
else: 
    print x, "is odd"
```

If the condition evaluates `False`, the `else` branch executes (if it's defined). Together `if` and `else` are called **branches**.

### Chained conditionals

When there are `> 2` number of conditions, we can add `elif` branches and create a **chained conditional**.

```Python
if x < y: 
    print x, "is less than", y 
elif x > y: 
    print x, "is greater than", y 
else: 
    print x, "and", y, "are equal"
```

Each condition is checked in the order defined, once one evaluates `True`, the other branches, even though they could be `True, do not get executed.

Conditional can also be **nested** within one another.

### The `return` statement

The `return` statement terminates the execution of a function before you reach the end. One use is to detect errors.

```Python
import math 

def printLogarithm(x): 
  if x <= 0: 
    print "Positive numbers only, please." 
    return # if it reaches this part, nothing below will get executed

  result = math.log(x) 
  print "The log of x is", result 
```

### Recursion

Functions not only can call each other, but also themselves. That is called `recursion`.

```Python
def countdown(n): 
    if n == 0: 
        print "Blastoff!" 
    else: 
        print n 
        countdown(n-1)
```

Functions that are calling themselves are said to be *recursive*.

#### Stack diagrams for recursive functions

Every time a function gets called, Python creates a new function frame, which contains the functions local `variables` and `parameters`. For a recursive function, there might be more than one frame on the stack at the same time.

This figure illustrates `countdown(3)`:

![recursive stack](http://dl.dropbox.com/u/31042440/recursive-function-stack.png)

As usual, the top of the stack is the frame for `__main__`. It is empty because we have no variables in `__main__`.

#### Infinite recursion

If a function never reaches its *base case* - that is know as **infinite recursion**, a minimal example:

```Python
def recurse(): 
    recurse()
```

In most programming environments there is a recursion limit, if it is reached we get a `RuntimeError: Maximum recursion depth exceeded`. It is changeable.

#### Keyboard input

Python 2.7.* has two user input methods

1. `raw_input` - always returns a string of what the user keyd in before pressing `enter`
2. `input` - uses `eval` on the same input
