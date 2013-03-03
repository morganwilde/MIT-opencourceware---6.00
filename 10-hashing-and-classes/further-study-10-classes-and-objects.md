Classes and Objects
===================

### User-defined compound types

With `Classes` you can create your own Python types.

`class` - a user-defined compound type.

```Python
class Point:
    pass
```

By creating the `Point` class, we created a new type called `Point`. Members of this type are called **instances** of the type. Creating a new instance is called **instantiation**, we do it like so:

```Python
blank = Point()
print type(blank)
# <type 'instance'>
print blank
# <__main__.Point instance at 0x1f01320>
```

A function like `Point()` that creates new objects is called a **constructor**.

### Attributes

We can add new data to an instance using dot notation:

```Python
blank.x = 3.0
blank.y = 4.0
print blank.x, blank.y
# (3.0, 4.0)
```

`x` and `y` in this case are called `Point` object attributes.

*Dot notation* is used for the purpose of referring to object unambiguously.

### Instances as arguments

You can pass an instance as an argument in the usual way:

```Python
def printPoint(p):
    print '(' + str(p.x) + ', ' + str(p.y) + ')'
```

`printPoint` takes a point as an argument and displays it in the standard format.

### Sameness

Objects by default have a certain type of sameness, or equality, called **shallow equality**.

```Python
p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
print p1 is p2
# False
p2 = p1
p1 is p2
# True

To compare the contents of objects - **deep equality** - we can write a function called `samePoint`:

```Python
def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)
p2 = Point()
p2.x = 3
p2.y = 4
print samePoint(p1, p2)
# True
```

### Instances as return values

Functions can return instances - `return Point()`

### Objects are mutable

We can change the state of an object by making an assignment to one of its attributes.

```Python
p1.x = 3.5
p1.y = 4.5
```

### Copying

The `copy` module contains a function called `copy` that can duplicate any object:

```Python
import copy
p2 = copy.copy(p1)
print p1 == p2
# False
print samePoint(p1, p2)
# True
```

The method `copy()` is sufficient when copying objects without references to other objects. But `deepcopy()` is needed when doing a complete copy that doesn't leave references between the two copies to the same objects.
