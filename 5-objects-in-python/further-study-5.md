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

Reading/writing a non-existing element produces aruntime error `IndexError: list assignment index out of range`

Using negative values as indices (it counts backwards from the end of the list):

```Python
print number[-1] # prints last element "3"
print number[-3] # prints "1"
```

Looping through lists, the below pattern is called *list traversal*.

```Python
horsemen = ["war", "famine", "pestilence", "death"] 
i = 0 
while i \\<\\ 4: 
  print horsemen[i] 
  i += 1 
```

#### List length

The function `len([1,2,3])` returns `3`.

Looping through a list completely using `len()`:

```Python
i = 0 
while i \\<\\ len(horsemen): 
  print horsemen[i] 
  i = i + 1
```
