Efficiency and Order of Growth
==============================

Before now it was all about getting a program to work. From now on it will be about making them work efficiently.

Key take-aways:

* Understanding why something is running
* How to avoid running forever

Efficiency is rarely about clever coding. It's really about choosing the right algorithm, I.e. **efficiency is about algorithms not coding details**.

Problem reducing. When confronted with a problem, try to reduce it to a previously solved problem.

We think about efficiency using two dimensions:

1. Space
2. Time

Usually it's a tradeoff.

### Computational complexity

How long something runs? That is influenced by (*why we shouldn't measure program time by timing them*):

* Speed of the machine
* Cleverness of Python implementation
* Depends upon the input

A better method is to count basic steps. `T: N->N`, `N` - size of the input, `->N` - number of steps it took.

A **step** is an operation with constant time.

```Pyton
# constant time examples
a = value
a[key]
```

Model of the computer - Random Access Machine (RAM).  
1. In this machine instructions are sequential
2. We assume constant time to access memory

#### How long something runs

Thinks of:

* Best case
    - I.e. first search in linear search is the answer
    - *don't focus on this*
* Worst case
    - It isn't there, so we look at each element up to the last one
    - *focus on this*
* Expected case
    - *too difficult to focus on this*
    
The worst case provides an upper bound to what can be expected. It also happens often.

#### example

```Python
# Factorial function
def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
```

Number of steps  
* 2 steps
* 3 * n steps
* 1 steps

What we care about here is `Growth` with respect to size of input (so we ignore 2 + 1). We even can ignore multiplicative constants.

We use asymptotic growth. It is writen using the `Big Oh` - `O(n)`. This gives us an upper bound for the asymptotic growth.

`f(x) is O(x**2)` - The function `f()` grows no faster than the quadratic polynomial `x**2`.

##### examples of `O()`

* O(1) - constant
* O(log n)
* O(n) - linear
* O(n log n) - log linear
* O(n**c) - polynomial
* O(c**n) - exponential

The moral - try and not do anything that is less speedy than `n log n`.

`F(x) is O(x**2)` - the worst case is about `x**2`.

#### example 2

```Python
def fact(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return n*fact(n - 1)
```

In this case we care about the number of times `fact()` is called.

#### example 3

```Python
def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
```

Nested loops.

1. find how many times the inner most loop will run
2. find how many times the outer most loop will run

So the complexity is `O(n**2)`. First start from the inside and work your way out.

#### example 4

```Python
def h(x):
    assert type(x) == int and x >= 0
    answer = 0
    s = str(x)
    for c in s:
        answer += int(c)
    return answer
```

Complexity would be the number of digits in `n`. So `O(log 10 (x))`.

#### example 5 - linear search/binary search

```Python
# linear
def search(L, e):
    for elem in L:
        if elem == e:
            return True
        if elem > e:
            return False
    return False
# binary
def bSearch(L, e, low, high):
    global numCalls
    numCalls += 1
    if high - low < 2:
        return L[low] == e or L[high] == e
    mid = low + int((high - low)/2)
    if L[mid] == e:
        return True
    if L[mid] > e:
        return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)
```

`O(n) where n is len(l)`

When looking at complexity, be careful to see if each step is **actually is done in constant time**.
