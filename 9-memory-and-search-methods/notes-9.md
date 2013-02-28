Memory and Search Methods
=========================

An `int` occupies 4 units of memory. How do we get to ith unit, I.e. location of `L[i]`?

- Start + 4 * i. This implementation depends on the fact that each element is of the same size, in this case `4`.

Python `list` is not like this.

`Linked list` - lisp uses it (old idea). Every element in a list is a pointer to next element, value. For a linked list, the big O is `O(i)`.

Instead of such an architecture, Python uses something like this:

![Python list memory](http://dl.dropbox.com/u/31042440/python-list-memory.png)

### Indirection

A `list` is a list of pointers of the same size. Now to find an object with key `i` you have to take only one step. This is how lists work in all `OOP` - Object Oriented Programming languages.

The concept of indirection is very powerful and used a lot.

Binary search is `O(logn)`. There is a catch - an asumption that the list is sorted, if that is not true - binary search doesn't work.

Does that always makes sense for the point of efficiency?

1. Sort L - `O(?)`
2. Use binary search - `O(log(len(L)))`
    - If the list isn't sorted, regular search would be `O(L)`

Is `O(?) + O(log(len(L)))` < `O(L)`, if not, that doesn't make sense. For that to be the case, we would need to be able to sort a list in less than linear time. And sort is never sub-linear time.

The reason we are interested in binary search is **amortized complexity**. If we sort the list once and search it many times, when enough searches are made, it makes sense to use binary search.

### Amortized complexity

If we plan on k searches we need to figure out - `O(sort(L)) + k * log(len(L)) < k * len(L)`. In practice `k` is very big. How well can we do `sorting`?

### Sorting

Bubble sort is almost always the wrong answer.

**Selection sort** - depends on establishing and maitaining an *invariant*. Invariant is something that's invariantely true. We take a pointer and devided that list into a prefix & suffix, and `inv = prefix is sorted`.

For a list such as `4, 2, 3`  
Next step `2, 4, 3`  
Next step `2, 3, 4`

```Python
def selSort(L):
    """Assumes that L is a list of elements that can be compared
       using >.  Sorts L in ascending order"""
    for i in range(len(L) - 1):
        #Invariant: the list L[:i] is sorted
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
        print 'Partially sorted list =', L
```

What is the complexity of **selection sort**. Each iteration I'm looking in every element in the suffix. `n = len(L)` and the big O is `O(n**2)`.

### Divide & conquer in sorting

1. Choose a threshold input size, n0, smallest problem
2. How many instances at each division
3. Combine the sub-solutions

#### Merge sort

Given to sorted lists you can merge them quickly.

`[1,5,12,18,19,20]` merge it with `[2,3,4,17]`.

`[1,2,3,4,5, ..., 20]`

The number of copies is `O(len(L))`, the number of comparisons at most `O(len(L_longer))`. So the Big O is linear.

That is the merge. We are going to call it `log(len(L))`, so the total complexity of the merge sort is `O(n * logn)`.

```Python
def sort(L, lt = lambda x,y: x < y): # lambda is the sorting mechanism
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2: # >
        return L[:]
    else:
        middle = int(len(L)/2)
        left = sort(L[:middle], lt)
        right = sort(L[middle:], lt)
        print 'About to merge', left, 'and', right
        return merge(left, right, lt)
```

`lambda` - a way to dynamically built a function on the fly. Using functional arguments is very powerful.
