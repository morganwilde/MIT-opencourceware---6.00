Unordered collections of unique elements
========================================

The `sets` module provides classes for constructing and manipulating unordered collections of unique elements.

Common uses include:

1. membership testing
2. removing duplicates from a sequence
3. computing math operations such as *intersection*, *union*, *difference*, and *symmetric difference*.

`sets` support:

```Python
from sets import Set
from sets import BaseSet
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
x in engineers:
    print x
# 'John', 'Jane', 'Jack', 'Janice'

print len(set)
# 4

print 'John' in engineers
# True
```

`sets` do not support indexing, slicing or other sequence-like behavior.

To determine if something is a set - `isinstance(obj, BaseSet)`.

More here [python docs sets](http://docs.python.org/2/library/sets.html)
