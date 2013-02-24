Recitation 2: Loops, Tuples, Strings and Functions
==================================================

###Loops:  
1. while
2. for

###Tuple
A non-scalar data type, that can hold many other elements.

```Python
tuple_literal = (1, 3.14, 'abc')
```

They are also immutable, thus syntax produces an error:
```Python
tuple1 = (1, 2, 3)
tuple1[0] = 9
# TypeError: 'tuple' object does not support item assignment
```

###String
A non-scalar and also immutable object type. Strings support iteration, slicing and many other functions, I.e.:  
* `string.upper()`
* `string.lower()`
* `string.find()`
* `string,replace()`

**Break** - it stops the inner most loop.

###Functions

An example of a function definition:

```Python
def cube(number):
    """Takes a number and returns the cube of that number.
    Input: number (float or int)
    Output: number (float)"""
    return number**3
```

Print is not return and vice versa.

**Functions** as everything else in Python, **are also objects**.
