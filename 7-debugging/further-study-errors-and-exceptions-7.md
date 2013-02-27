Errors and Exceptions
=====================

There are (at least) two distinguishable kinds of errors:

1. *syntax errors*
2. *exceptions*

### Syntax errors

```Python
while True print 'Hello world'
#File "<stdin>", line 1, in ?
#   while True print 'Hello world'
#                  ^
#SyntaxError: invalid syntax
```

This is the most common novice user caused type of error.

### Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. These errors are called **exceptions** and are not unconditionally fatal, I.e. you can handle them in your program. If it isn't handled it produces error messages:

```Python
10 * (1/0)
# ZeroDivisionError: integer division or modulo by zero
4 + spam*3
# NameError: name 'spam' is not defined
'2' + 2
# TypeError: cannot concatenate 'str' and 'int' objects
```

The word inside the comments before the colon is called the *exception type*, and they are built-in identifiers (not reserved keywords).

#### Handling exceptions

It is possible to handle selected exceptions using the `try` statement, example:

```Python
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
```

The `try` statement works as follows:

* The `try` clause (the statement block between `try` and `except`) is executed
* If no exception occurs, `except` block is not executed and `try` statement is finished
* If an exception occurs, the rest of the `try` block is skipped, then if `exception` type matches the one in the `except` statement, the `except` block is executed without stoping the program
* If an exception occurs and it doesn't match the one described in the `except` clause, it is passed to outer `try` statements; if no handle is found - it is an *unhabled exception*; execution stops with a default message

A `try` statement may have more than one `except` clause:

```Python
except (RuntimeError, TypeError, NameError): # Tuple form required
    pass
```

You can also have a wildcare `except` clause that catches everything `except:` - use with **caution**!

Using an optional `else` clause. It executes only if the `try` clause didn't raise an exception.

```Python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
```

This is helpful because it minimises the amount of code in `try` that can cause the exception, so this allows for more precision.

When an exception occurs, it may have an associated value, aka *argument*; its presence depends on the exception type.

```Python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)    # the exception instance
    print inst.args     # arguments stored in .args
    print inst          # __str__ allows args to printed directly
    x, y = inst.args
    print x
    # 'spam'
    print y
    # 'eggs'
```

#### Raising exceptions

`raise` statement allows the programmers to force a specified exception to occur.

```Python
raise NameError('HiThere')
# NameError: HiThere
```

You can use `raise` to reraise the last exception in the `except` clause:

```Python
try:
    raise NameError('HiThere')
except NameError:
    print 'An exception flew by!'
    raise
# NameError: HiThere
```

#### User-defined exceptions

Programs may name their own exceptions by creating a new exception class. They should be typically derived from the `Exception` class.

```Python
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value

# My exception occurred, value: 4
raise MyError('oops!')
# __main__.MyError: 'oops!'
```

In this exampe, the default `__init__()` of Exception has been overridden. This behavior creates the `value` attribute while replacing the default behavior of `args` attribute.

When creating a module that can raise several distinct errors, a common practice is to create a base `class` for exceptions defined by that module, and `subclass` for specific error conditions:

```Python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
```

Most exceptions are defined with names the end in **"Error"**.

#### Defining Clean-up Actions

The `try` statement has one more optional clause - `finally`. It is intended to define clean-up actions that must be executed under all circumstances.

```Python
try:
    raise KeyboardInterrupt
finally:
    print 'Goodbye, world!'
# Goodbye, world!
# KeyboardInterrupt
```

A `finally` clause is always executed before leaving the `try` block. When an exception has occured in the `try` clause has not been handled by an `except` clause (or it occured in `except` or `else` blocks), it is re-raised after the `finally` clause has been executed.

```Python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
        
divide(2, 1)
# result is 2
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause
divide("2", "1")
# executing finally clause
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

In real world applications, `finally` statement is useful for releasing external resources (files/network connections), regardless is they were used/not.

#### Predifined Clean-up Actions

```Python
with open("myfile.txt") as f:
    for line in f:
        print line,
```

After the statement is executed, the file `f` is always closed no matter what.
