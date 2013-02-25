Dictionaries
============

The `non-scalar` types - `str`, `list`, `tuple` - use integers as indices.

Dictionary is similar in many ways to a `list` except that they can use any immutable type as an index (yes, `tuple` also can be a `dict` key) and unordered.

```Python
eng2sp = {} # creates a dict object 'eng2sp'
eng2sp['one'] = 'uno' # mutates the object
eng2sp['two'] = 'dos'
```

#### Dictionary operations

```Python
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['pears'] = 0 # mutates the object to change value to 0 of the key 'pears'
del inventory['pears'] # mutates the object to remove key, value pair with key 'pears'

print len(inventory) # 3
```

#### Dictionary methods

A **method** is similar to a function - takes arguments and returns a value - but the syntax is different. For example:

```Python
# instead of this
keys(eng2sp)
# we do this
eng2sp.keys()
```

This form of dot notation specifies the name of the function, `keys`, and the name of the object to apply to, `eng2sp`. A method call is called an **invocation**; in this case we are invoking `keys` on the object `eng2sp`.

Other methods:

* `eng2sp.values()` - returns values
* `eng2sp.items()` - returns key, value pairs in form of tuples as a list
* `eng2sp.has_key('one')` - returns `True` if object has key `'one'`

#### Aliasing and copying

Because `dict` is a mutable type, aliasing has the same rules as with lists.

To instead **copy** a list, when assigning to a name, use the method `copy()`, I.e. `copy = someDict.copy()`.

#### Sparse matrices

A `list` representation of a particular matrix with a lot of zeroes:

```Python
matrix = [ [0,0,0,1,0], 
           [0,0,0,0,0], 
           [0,2,0,0,0], 
           [0,0,0,0,0], 
           [0,0,0,3,0] ]
```

An alternative way to describe the same matrix using a `dict`:

```Python
matrix = {(0,3): 1, (2, 1): 2, (4, 3): 3}
# to achieve the same results as with the list, when calling elements of such matrix, use .get method
print matrix[1,3]
# KeyError: (1,3)
print matrix.get((1,3), 0)
# 0
```

#### Long integers

Python provides a type called `long` that can handle any size integer.

```Python
print type(1L)
# <type 'long'>
print long(1)
# 1L
```

Python does automatic type conversion whenever it detects an overflow and returns the result as a long integer.
