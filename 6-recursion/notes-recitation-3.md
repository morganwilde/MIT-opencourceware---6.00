Lists and their elements, sorting an recursion
==============================================

Lists
_____

What is the difference between a `list` and a `tuple`:

* `list` - mutable
* `tuple` - immutable

When assigning to a slice of a `list` be careful using the following syntax:

```Python
list = [1,2,3]
# "3:3" is here >= number of the last element
list[3:3] = 4
# TypeError: can only assign an iterable
list[3:3] = [4]
# list = [1, 2, 3, 4]
list[1:1] = [450]
# list = [1, 450, 2, 3, 4]
```

Assigning and removing list items using methods

```Python
list = [1,2,3]
list.append(4)
# list = [1, 2, 3, 4]
list.remove(1)
# list = [2, 3, 4]

# remove the very last values of a list
list.pop()
# list = [2, 3]

# merges the iterable object provided in the paremeter with the object `list`
list.extend([10, 20])
# list = [2, 3, 10, 20]
```

To create an empty list we have a few options

```Python
list = [0]*10
# list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list = [[]]*10
# list = [[], [], [], [], [], [], [], [], [], []]
```

Lists when working with matrices

To access multi-dimensional matrices `matrix['row']['column']`

#### How are lists stored in the memory

`list = [0,1,'apple']`

The diagram below demonstrates why you can mutate the list. The reason is the list itself is not a collection of objects, but of references to objects in memory.

![list memory](http://dl.dropbox.com/u/31042440/list-stored-in-memory.png)

#### Aliasing

If you assign two names to a list, I.e. `a = b = [1,2]`, `a` and `b` will both be aliases for the same list object, thus changing one, you will access the same changes with the other name.

#### Converting lists to tuples and vice versa

Just use the built in `type()` functions, I.e. `list(tuple)` or `tuple(list)`.

Dictionaries
____________

Using dictionaries is not irreplaceable as a data type, but it is useful because of the built-in methods it has in Python.

Dictionary `key` has to be unique to it.

Items in a dictionary are not ordered.

#### Ordering (using sort)

```Python
dict = {'a': 1, 'c': 3, 'b': 2, 1: 4}
keys = dict.keys()
keys.sort()
# [1, 'a', 'b', 'c']
```

Recursion
_________

The principle behind recursion is breaking down the problem into a base case and an inductive case.

#### Example using a factorial

n! = n(n-1)!

1. The base case - `if n == 0: return 1`
2. Inductive case - `else: return n * factorial(n-1)`

#### Fibonacci

1. base case - `if n <= 1: return 1`
2. inductive case - `return f(n-1)+f(n-2)`

#### Recursive exponentiation

`3**10 = 3 * 3**9`

1. base case - `if n == 0: return 1`
2. recursive case - `m**n = m * m**n-1`

#### Recursive multiplication

`3*5 = 3 + 3*4`

1. base case - `if n == 0: return 0`
2. recursive case - `m*n = m + m(n-1)`
