Lists and their elements, sorting an recursion
==============================================

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
