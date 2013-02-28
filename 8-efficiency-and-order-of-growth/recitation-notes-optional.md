Algorithm Complexity and Class Review
=====================================

Why we do `O()` notation? It gives us an upper bound on how long something is gonna run. It doesn't measure time, but the amount of steps it takes to complete the program with relation to input.

Why is that important? `O()` notation is not concerned with small inputs and can be wrong on what is fastest on them, but it will always be right on big inputs.

With `O()` you can compare two algorithms and makes educated guess on which one will be faster.

If an alogrithm doesn't depend on the input - it is always `O(1)`.

When graphing *Big O* notation, the difference between different types of `O()` is very clear.

A single line of code can generate big differences in number of steps, while complex code might still be constant.

First define what `n` is, then provide the `O(n)` notation.

#### Example

```Python
def count_same_ltrs(a_str, b_str): 
    count = 0 
    for char in a_str: # O(n)
        if char in b_str: # O(m)
            count += 1 
    return count
```

So compound of this in `O()` is `O(nm)`.

Operations like `slicing` and `copying` are not constant time.

How to figure out the *complexity* of a recursive function.

1. Find out how many times you're making a recursive call.
2. If it calls itselft `n` times, it's `O(n)`

#### Fibonacci example

Is `O(2**n)`.
