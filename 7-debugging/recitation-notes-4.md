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

Another version of this function, but defined iteratively:

```Python
def iter_mult(m, n):
    """
    m and n are integers
    """
    if n == 0 or m == 0:
        return 0
    # Initialize variable to hold result
    result = 0
    if n >= 1:
        while n > 0:
            # Add 'm' to the result for 'n' times
            result += m
            n -= 1
    elif n <= -1:
        # n is negative, so we want to increment n
        while n < 0:
            # Add '-m' from the result for 'n' times
            result += -m
            n += 1
    return result
```

A recursive fibonacci example:

```Python
def rec_fib(n):
    """
    A recursive function to find the nth fibonacci number
    n is an int >= 0
    """
    # Base case: 0th fib number is 0 or 1
    if n == 0 or n == 1:
        return n
    # Recursive case: nth fib number is sum of (n-1) and (n-2) fib numbers
    else:
        return rec_fib(n-1) + rec_fib(n-2)
```

Iterative version of the same function

```Python
def iter_fib(n):
    """
    """
    # Fib(0) = 0, Fib(1) = 1
    if n == 0 or n == 1:
        return n
    # Fib(n) = last fib number + fib number before
    else:
        # Hold the current and previous Fibonacci numbers
        previous_fib = 0
        current_fib = 1
        for iteration in xrange(1, n):
            next_fib = current_fib + previous_fib
            # save these values
            previous_fib = currentfib
            current_fib = next_fib
    return current_fib
```

This is the case where the `recursive` version is easier to understand.

### Bisection search

`recitation-code-4.py` has both the iterative and recursive examples of bisection search. This case is where the recursive technique makes for easier understand of the function.

Computer programming is a game of trade-offs, where your trading off memory for speed and so on.

### Floating point

Floating points are not exact. So we can't compare them exactly.

```Python
one_100 = 1/100.0
nine_100 = 9/100.0
ten_100 = 10/100.0
print ten_100 == (one_100+nine_100)
# False
print repr((one_100+nine_100)) # this is how Python deals with that number
# '0.09999999999999999'
```

So the way to deal with floating numbers is to always test the answer against `epsilon` - a certain margin of error we are willing to accept.

How to determine the size of `epsilon` depends on your program needs, I.e. how precise of an answer do you need. `epsilon` does have a limit depending on language and hardware.

Even though floating points are not exact, they are consistent. So if you add a floating point and subtract the same floating point, the number will remain the same.

`IEEE 754` - the standard for binary floats

### Pseudo code

A lot of the difficulty when writing new programs - we don't naturally think in a computer language, but a human language. Pseudo code provides and intermediary stage.

#### Pseudo code for hangman

```Pseudocode
hangman
- select random word
- while we have guesses remaining and the word is not guessed
    - tell how many letters
    - display a masked version of word
    - tell remaining letters
    - ask for a letter
    - check if it is in the word
        - if it is add to correct letters guessed
        - else remove the letter from letters remaining
            - tell the user they're wrong
```

The above pseudo code describes the solution in human terms to the hagngman problem. This is a good way to start thinking about the problem before you start coding.

#### Prime number function

```Pseudocode
1. test # if equal to 2,3
    - if equal return true
2. start at 5
    - test if n % 5 == 0
        - if it is then return false
        - else goto 7
    - test if n % 7 == 0
        - -//-

# the above example shows a good case to put a loop there

x = 5
while x less than sqrt(n)
    test if x evenly devides n (n%x == 0)
        if it does return false
    add 2 to x
return true
```

### Debugging

Debugging is finding mistakes. Why your code is doing what it does - the question to ask always. It is mostly experience, not a natural human skill. Then you need to devise tests that test the program in different test cases.

When you think you found a bug and know how to correct it, you want to try and make as few changes before another test to see if you haven't introduced new bugs.

`Test harness` - a common name for the tests you devise for your program. They way to use test harnesses is to use them everytime you make changes to the program.
