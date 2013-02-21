Introduction to 6.00
====================

Computational problem solving
-----------------------------

Two kinds of knowledge:
1. Declarative
    - Statements of fact - a good health care plan improves the quality of medical care while saving money
    - y is the square root of x if y*y=x
2. Imperative
    - it's how to solve a problem, I.e. a recipe
    - this pseudo code example:
> 1. start with a guess - g
> 2. if g*g is close enough to x, then g is the answer
> 3. else generate a new guess by averaging g and x/g (G-new = (G-old + x/G-old)/2)
> 4. with this new guess go back to step 2

This example is an algorithm - how to perform a computation. When it halts - the algorithm has converged. It's a set of instructions + a flow of control + a termination condition.

Machines
--------

The first computers were **fixed program computers**. Designed to do very specific things and that's it.
What we now have today are **stored program computer**. It's basic idea is that instructions are the same as data. So now a pc is like an interpreter - executing any set of legal instructions you give it.

![A model pc](http://dl.dropbox.com/u/31042440/what-is-a-computer.jpg)

There are 6 primitive instructions operating with 1 bit of information. A programing language provides a set of instructions and a flow of control and how do you combine them (the main distinguishing factor of languages). The computer will always do what you tell it to do.

Languages
---------

1. Interpreted - source code > checker > interpreter > output
2. Compiled - source code > checker/compiler > object code > interpreter > output

Language is:

1. Syntax
    - Which sequences of characters and symbols constitute a well-formed string (x = 3 + 4)
2. Static semantics
    - Which well-formed strings have a meaning (3/'abc' - syntax OK, but there is a static semantics error)
3. Semantics
    - What the meaning of a well-formed, meaningful string is. The main issue related to semantics is programs doing a different thing than the one intended

What happens with semantic errors
- Crash (when this happens, make sure this is local, I.e. not affecting other parts of program)
- Never stop (aka infinite loop, that's an error in flow of control)
- Run to completion and produce the wrong answer

Good features of python
1. Easy to learn
2. Very widely used today (especially in life sciences)
3. Easier to debug than most languages (because it's an interpreted language)
