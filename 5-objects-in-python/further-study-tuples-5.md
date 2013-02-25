Tuples
======

#### Mutability and tuples

The `tuple` Python type is similar to a `list` except that it is immutable. Syntactically, a tuple is a comma-separated list of values

```Python
tuple = 'a', 'b', 'c', 'd', 'e'
tuple = ('a', 'b', 'c', 'd', 'e') # a more common notation, even though it is not necessary
t1 = ('a',) # to create a single element tuple
```

Operations on `tuples` are the same as with `lists`.

#### Tuple assignment

Instead of

```Python
temp = a
a = b
b = temp
```

We can use a form of *tuple assignment* - `a, b = b, a`, all the expressions on the right side are evaluated before any of the assignments. The number of variables on both sides **has to be same**.

#### Random numbers

Most computer programs are said to be **deterministic**. Python has a built-in function that generates **pseudorancom** numbers, which are not truly random in the mathematical sense.

Python has the module `random` to do random numbers
