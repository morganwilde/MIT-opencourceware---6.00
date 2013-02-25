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

![two possibilities](http://dl.dropbox.com/u/31042440/name-object-assignment.png)

1. In one case, `a` and `b` refer to two different things that have the same value.
2. In the second case, they refer to the same thing.

These "things" are called **objects**. Every object has a unique **identifier**, which can be obtained with the `id()` function. By printing the identifier of `a` and `b`m we can tell whether they refer to the same object.

`id()` returns the object's memory address.

```Python
print id(a)
# 19368048
print id(b)
# 19368048
print a is b
# True
```

In fact, we get the same identifier twice, which means that Python only created one string, and both `a` and `b` refer to it.

Lists behave differently, when creating to identical lists, we get two objects:

```Python
a = [1,2,3]
b = [1,2,3]
print id(a)
# 21817824
print id(b)
# 21852960
print a is b
# False
```

The state diagram looks like this:

![state diagram](http://dl.dropbox.com/u/31042440/list-name-object-assignment.png)

`a` and `b` have the same value, but do not refer to the same object.

#### Aliasing

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:

```Python
a = [1,2,3]
b = a
print b is a
# True
```

![aliasing](http://dl.dropbox.com/u/31042440/list-aliasing.png)

The key with aliasing mutable objects is that changes made using one alias with effect all other aliases. Immutable objects don't have this property, since you cannot make any changes to them.

#### Cloning lists

```Python
a = [1,2,3]
b = a[:]
print b is a
# False
```

#### List parameters

Passing a list as an argument actually passes a reference to the list, not a copy. When it returns a list, it also returns a reference, not a copy.

```Python
def head(list): 
    list[0] = 50
numbers = [1,2,3]
head(numbers)
print numbers
# [50, 2, 3]
```

What happens in the example above can be displayed like so:

![list parameters](http://dl.dropbox.com/u/31042440/list-as-parameters.png)

#### Nested lists

```Python
list = ["hello", 2.0, 5, [10, 20]]
print list[3][1]
# 20
```

They are also often used to represent matrices, like so:

```Python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print matrix[1]
# [4,5,6]
print matrix[1][1]
# 5
```

#### Strings and lists

The `string` module has, among other things, `split()` and `join()` methods.

```Python
import string
song = "The rain in Spain..."
print string.split(song) # by default any number of " " is used as the delimeter
# ['The', 'rain', 'in', 'Spain...']
print string.split(song, 'ai') # custom delimeter 'ai'
# ['The r', 'n in Sp', 'n...']
list = ['The', 'rain', 'in', 'Spain...']
print string.join(list) # default " " as the delimeter
# 'The rain in Spain...'
print string.join(list, '_') # custom "_" delimeter
# 'The_rain_in_Spain...'
```
