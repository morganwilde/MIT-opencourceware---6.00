Objects in Python
=================

### Data structures
_______________

As per example:

1. **Tuples**
2. **Lists**
3. **Dictionaries**

**Tuples** and **Lists** are _ordered_ sequences of objects.

### Tuples

**Tuples are immutable**.

```Python
# Tuples
Test = (1, 2, 3, 4, 5)
print Test[0]
print Test[1]
print Test
print Test[-1] # 5
```

Tuples can be sliced, I.e. subsequences of a tuple can be called using `Test[1:2]` will give the slice `(2,)` of the tuple `Test` (indeces 1 through 2)

### Lists

**Lists are mutable**, once you create a list, you can change it.

```Python
Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = []
Univs.append(Techs)
print 'Univs =', Univs
# Univs = [['MIT', 'Cal Tech']]
```

**Append()** is what Python calls a *method*. They can be thought of as being a different form of a function, I.e.:

```Python
append(List, element)
List.append(element) # mutates the list, it has a side effect
```

What `Univs` prints out is a list, with a list `Ivys` being appended to the end of the list `Univs`.

Iterating over a list

```Python
Univs.append(Ivys)
for e in Univs:
    print 'e =', e
#e = ['MIT', 'Cal Tech']
#e = ['Harvard', 'Yale', 'Brown']
```

Sorting (in this case it sorts `flat` in alphabetical order)

```Python
flat = Techs + Ivys
flat.sort()
print 'flat =', flat
```

Changing lists. It doesn't assign a new value to the identifier `flat[1]`, it changes the object.

```Python
flat[1] = 'UMass'
flat.remove('Brown')
```

* _Assignment_ has to do with binding of names to objects  
* _Mutation_ has to do with changing the value of objects

```Python
L1 = [2] # bounds 'L1' of length 1 to a list object '[2]'
L2 = [L1, L1] # bounds 'L2' of length 2 to a list object '[L1, L1]'
print 'L2 =', L2 # [[2], [2]]
L1[0] = 3 # mutate L1
print 'L2 =', L2 # [[3], [3]]
L2[0] = 'a' # mutate the object 'L2', so that its first element is no longer 'L1', but the string 'a'
print 'L2 =', L2
```

An example showing the difference between assignment and mutation.

```Python
L1 = [2]
print 'L2 =', L2
# L2 = ['a', [3]]
```

The reason `L2` doesn't change is because `L1` has been assigned a new object, the list `[2]`. Since the old assignment `L1` has been destroyed, what is left in `L2` is the last mutated object previously pointed to by `L1` before its name has been reassigned.

An example of an alias, and single object with multiple names and its perrils.

```Python
def copyList(LSource, LDest):
    for e in LSource:
        LDest.append(e)
        print 'LDest =', LDest

L1 = []
L2 = [1,2,3]
copyList(L1, L1) # creates an infinite loop
```

### Dictionary

The dictonary elements are not ordered and the indices don't have to be integers and they are called `keys`. A `key` can be any immutable type object.

```Python
D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
D1 = D
print D1
D[1] = 'uno'
print D1
for k in D1.keys():
    print k, '=', D1[k]
```

A `dict` is a set of `key, value` pairs, we access `values` using their `keys`.

```Python
EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats': 'mange', 'drinks': 'bois',\
        'likes': 'aime', 1: 'un',\
        '6.00':'6.00'}
print EtoF
# {1: 'un', '6.00': '6.00', 'eats': 'mange', 'likes': 'aime', 'bread': 'du pain', 'drinks': 'bois', 'wine': 'du vin'}
print EtoF.keys()
# [1, '6.00', 'eats', 'likes', 'bread', 'drinks', 'wine']
print EtoF.keys
# <built-in method keys of dict object at 0x1c30ff0>
del EtoF[1]
print EtoF
# {'6.00': '6.00', 'eats': 'mange', 'likes': 'aime', 'bread': 'du pain', 'drinks': 'bois', 'wine': 'du vin'}
```

The above example prints out the objects value in a different order than when it was assigned. The order of `dicts` is not defined by Python.

`del` is a command that mutates `EtoF` to remove the object located at key `[1]`.


