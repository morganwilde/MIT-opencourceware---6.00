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
