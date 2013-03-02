Hashing and Classes
===================

### Sorting and hashing

Hashing is how dictionaries are implemented in Python, but that comes with the cost in space.

Example of hashing a set of integers (quickly).

`hash(i)` -> converts i to some int within 0;k.

We put each `hash` into a list, aka The *bucket*.

#### Code example

```Python
def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    return hSet
```

Creates an empty bucket.

The hash function is many-to-one, aka an infinite amount of integers will hash to the same bucket. When two different object hash into the same bucket it is called a **collision**.

There are many ways to solve collisions, this example is called linear rehash.

Complexity of hashing is the length of the bucket.

A good hash function has the property that it widely disperses its values.

When people use **hash tables**, they make them big enough, so that the lookup time is `O(1)`. Python does such a thing with `dict` object type.

Any kind of immutable object can be hashed. This is the reason the keys in `dict` are immutable, so that the hash of the `key` stays the same no matter what.

#### A more complex hash

```Python
def hashElem(e):
    global numBuckets
    if type(e) == int:
        val = e
    if type(e) == str:
        #Convert e to an int
        val = 0
        shift = 0
        for c in e:
            val = val + shift*ord(c)
            shift += 1
    return val%numBuckets
```

This is the way pictures are compared when doing face-recognition, they are stored with an int hash and then each face is compared to a hash.

All hashing has to do is map an argument to an `int` value.

### Exceptions

Exceptions are everywhere in Python.

```Python
test = [1,2]
test[12]
# IndexError
```

That is an exception.

These kind of exceptions are called **unhandled exceptions** - they cause the program to crash.

Once a program is debugged this should never happen, because there is mechanism in Python that catch exceptions. And this method is a perfectly good *flow of control* method.

#### Try

```Python
try:
    # some code to try
    # if an exception is is raised, it immediatelly stops here
except:
    # executes the code is an exception has been raised
# continues executing
```

An example function

```Python
def readVal(valType, requestMsg, errorMsg):
    numTries = 0
    while numTries < 4: # >
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except ValueError:
            print(errorMsg)
            numTries += 1
    raise TypeError('Num tries exceeded')
```

This is very useful when dealing with user provided input, because it lets explain what happens to the user if something unexpected happens.

### Classes

It is a distinguishing feature of Python - a **class**.

We've already seen `module` - usually a collection of related functions. An example would be `import math`, which provides access to `math.log`. When using something imported, we use the *dot notation* to distinguish it from local functions. This avoids conflicts by disambiguing.

What a class is, it's like a `module`, but not only a collection of functions. It is a collection of *data* and *functions*. Functions that operate on that data. They are bound together.

#### Object Oriented Programming

We have seen similar functionality using `list`.

Data and functions associated with an objects are called its **attributes**.

Message passing metaphor.

When I write `L.append(e)`, I'm passing the message `append(e) to L, where it finds the meaning of the message and acts upon the meaning.

Method is a function associated with an object. In the case `C.area()` - `area()` is a method of `C`.

Just as data have types, objects also have types. A class is a collection of objects with identical characteristics, that creates a type.

So objects like `list`, `dict` are just built-in classes.
