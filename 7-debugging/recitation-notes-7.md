Recursion, pseudo code and debugging
====================================

### Recursion

It is a divide & conquer technique, that splits the problem into a smaller problem. It works by having a *base case* and a *inductive case*.

An example of `recursive multiplication`:

```Python
def rec_mult(m, n):
    # Base case (only occur if call the function with zero)
    if n == 0:
        return 0
    elif n >= 1:
        return m + rec_mult(m, n-1)
    elif n <= -1:
        return -m + rec_mult(m, n+1)
```


