Recursion
=========

Dictionaries. If say we didn't have dictionaries, we could use lists:

```Python
def keySearch(L, k):
    for elem in L:
        if elem[0] == k: return elem[1]
    return None
```

The key problem with this technique is that the amount of time needed to find the value associated with the key in a `list` is proportional to the size of the list.

Dictionary, on the other hand, has a constant search time, I.e. the search will last the same amount of time for `len({}) = 1` and `len({}) = n`.

#### Translate example

```Python
def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' '\
                          + translateWord(word, EtoF)
            word = ''
    # since sentences don't end with a space, it adds the final word
    return translation[1:] + ' ' + translateWord(word, EtoF)
```

Why write `translateWord()`?

Code division
_____________

1. It saves space in the code
2. Gives modular abstraction. Isolating the place where you can find/change the function/method.

Divide & conquer - taking a hard problem and braking it into smaller individual pieces, that:

1. small problems are easier to solve
2. solutions to small problems can easily be combined to solve the big problem

The technique of recursion
__________________________

* A way of describing or defining problems
* A way of designing solutions

This technique includes two parts

1. The base case
    - the direct answer
2. The inductive case
    - reduce to simple problem plus other simple operations
    
#### Exponentiation function

b**n = b x b... x b, with `n` number of `b`

In Python a recursive solution to that problem would be:

```Python
def simpleExp(b, n):
    if n == 0:
        return 1
    else:
        return b * simpleExp(b, n-1)
```

#### Tower of Hanoi problem

```Python
def Hanoi(n, f, t, s):
    # number of layers
    # from stack
    # to stack
    # spare stack
    if n == 1:
        print 'move from ' + f + ' to ' + t
    else:
        # take the larger stack and place it on the spare stack
        Hanoi(n-1, f, s, t)
        # take the smaller stack and place it on the target stack
        Hanoi(1, f, t, s)
        # take the larger block from the spare stack to the target stack
        Hanoi(n-1, s, t, f)
```

#### Palindrome check

If I have a string of length `1`, it is a palindrome.  
If it is longer than one, check the first letter and last to see if they are the same. If that is true, check the sedond and the second to last letter if they are the same.  

```Python
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])
```

The basic property of recursive methods is that you divide your problem into a base case and an inductive case.

#### Fibonacci numbers

Rabbit reproduction rates each month:

| Month | Females |
| -----:|:-------:|
| 0     | 1       |
| 1     | 1       |
| 2     | 2       |
| 3     | 3       |
| 4     | 5       |
| 5     | 8       |
| 6     | 13      |

This describes a recursive relationship.

`f(n) = f(n-2) + f(n-1)` - recursive case  
`if n <= 1: f(n) = 1` - base case

Python code:

```Python
def fib(x):
    """assumes x an int >= 0
        Returns Fibonacci of x"""
    assert type(x) == int and x >=  0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
```
