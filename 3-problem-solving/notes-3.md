Problem solving
===============

Difficulty of the problem

**Decrementing function**

1. Map a set of program variables to an integer
2. When the loop is entered for the first time, its value is non-negative
3. Whent its value <= 0, loop terminates
4. It's decreased each time through the loop

If such a function exists, the loop is guarenteed to terminate. In the case of the first loop in the handout, it's `abs(x) - ans**3`, so the steps would be when `x = 8`

1. 8 - 0 = 8
2. 8 - 1 = 7
3. 8 - 8 = 0 `# exit the loop`

The first algo in the handout is called *guess and check* and specifically - *exhaustive enumeration*. It exhausts the space of all possible answers. They are also know by the name of *Brute force*. They work because computers are fast.

For loop
________

**range(x, y)** gives values (x, x+1, ..., y-1).

Approximation
_____________

What does it mean to find a square root of a number. So this mean finding an answer that is good enough.

First we define how good of an approximation we need.

`Find a Y such that y*y = x +/- epsilon` - the specification of the problem.

The length of that algo depends on the size of the increment, epsilon, and the input.

Bisection search
________________

1. cut the search space in half each iteration.

The danger is when the answer lies outside of the range
