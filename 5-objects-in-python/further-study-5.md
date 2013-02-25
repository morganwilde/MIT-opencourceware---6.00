Lists
=====

Python `list` is an ordered set of values, where each value is identified by an index. They are similar to `strings`, except that `list` elements can have any type. They are also called *sequences*. `List` object is mutable.

#### List values

List literal notation:

```Python
[10, 20, 30, 40] 
["spam", "bungee", "swallow"]
["hello", 2.0, 5, [10, 20]] # the inner list "[10,20]" is said to be "nested"
[] # empty list
```

Creating lists using the `range()` function

```Python
range(1,5) # first parameter (start [optional]) is inclusive, second (end) is exclusive
# [1, 2, 3, 4]
range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Accessing elements

```Python
number = [1,2,3]
print number[0] # prints first element
number[1] = 20 # mutates the second element
print number[5-3] # any integer expression can be used as an index
# 3
```

Reading/writing a non-existing element produces a runtime error `IndexError: list assignment index out of range`

Using negative values as indices (it counts backwards from the end of the list):

```Python
print number[-1] # prints last element "3"
print number[-3] # prints "1"
```

Looping through lists, the below pattern is called *list traversal*.

```Python
horsemen = ["war", "famine", "pestilence", "death"] 
i = 0 
while i <\ 4: 
  print horsemen[i] 
  i += 1 
```

#### List length

The function `len([1,2,3])` returns `3`.

Looping through a list completely using `len()`:

```Python
i = 0 
    while i <\ len(horsemen): 
  print horsemen[i] 
  i = i + 1
```

#### List membership

`in` is a boolean operator that tests membership in a sequence, it works on any sequence (string, tuple, list). `not in` is used to test if an element is not a member of a sequence.

```Python
horsemen = ['war', 'famine', 'pestilence', 'death']
print 'pestilence' in horsemen
# True
print 3.1415 in horsemen
# False
```

#### Lists and `for` loops

```Python
for element in list:
    print element
```

#### List operations

* `+` - concatenates lists, I.e. `[1] + [2]` returns `[1,2]`
* `*` - repeats a list a given number of times, I.e. `[1] * 4` returns `[1,1,1,1]`

#### List slices

* `list[1:3]` - returns a list of elements from the first (exclusive) to the third (inclusive)
* `list[:4]` - returns all elements up to and including the fourth
* `list[3:]` - returns all elements from the third (while excluding the third)
* `list[:]` - returns the whole list

#### Lists are mutable

```Python
fruit = ["banana", "apple", "quince"] 
fruit[0] = "pear" # mutates the first element to the object 0
fruit[-1] = "orange" # mutates the last element
print fruit 
# ['pear', 'apple', 'orange']
fruit[0:2] = ["blue", "yellow"] # change a slice of the list at once
print fruit
# ['blue', 'yellow', 'orange']
# delete the first two elements
fruit[0:2] = [] 
del fruit[0:2]
```

To squeeze an element in between others, first select an empty slice and assign a value to it:

```Python
list = ['a', 'd', 'f']
list[1:1] = ['b', 'c']
print list
# ['a', 'b', 'c', 'd', 'f']
```

#### Objects and values

If we execute these assignment statements,

```Python
a = "banana"
b = "banana"
```

we know that `a` and `b` will refer to a string with the letters `"banana"`. But we can't tell whether they point to the *same* thing.

There are two possible states:

!(http://dl.dropbox.com/u/31042440/name-object-assignment)
