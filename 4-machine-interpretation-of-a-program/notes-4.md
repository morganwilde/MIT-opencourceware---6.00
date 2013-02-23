Machine interpretation of a program
===================================

The bisection search problem from last lecture (does it work for all inputs?).

```Python
x = 0.5
epsilon = 0.01
low = 0.0
high = max(x, 1.0) # max() is the fix that ends the infinite loop
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print 'ans =', ans, 'low =', low, 'high =', high # a way to see where the loop fails
    if ans**2 \<\ x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ans, 'is close to square root of', x
```

Most common problem in debugging programms is that people are lazy, I.e. not designing the test appropriatelly.

The issue with the top code example, is that the answer for fractions doesn't lie in the search spave.

Less code is better, because with the size of the codebase that difficulty in debugging it rises quadratically. So whenever there is a possibility to achieve the same thing with less code, that's the path to take.

The function
____________

They provide a mechanism that enables:

1. Decomposition - creates structure (allows to break the program up into modules)
    - Modules are self-contained and are reusable, that can be used in multiple contexts
2. Abstraction - supresses detail
    - It allows us to use a piece of code as a black box, this lets us use code that other people have written easily.

Functions let us brake up code. They let us extend the language by adding new primitives, that we can use just as built in primitives.

```Python
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon ints or floats.  epsilon > 0.0
       returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon
```

The structure goes like this:

1. `def` - starts the definition of a function
2. `withinEpsilon` - the name, which followes def immediatelly
    - A good rule in naming functions - give them mnemonic names so that it is easy on infer their meaning
3. `(x, y, epsilon)` - and in the parentheses we have formal parameters
4. `:` - after the colon and a newline followed by a tab, we have the body of the function
5. `"""explanation"""` - a way to abstract the meaning and products of the function

A few runs of the function:  
```Python
print withinEpsilon(2,3,1)
# True
val = withinEpsilon(2,3,0.5)
print val
# False
```

If the function doesn't have a `return` somewhere inside its body, if we print out the value of a call to such functions, we will see `None` being returned.

##What happens when we call a function##

```Python
def f(x):
   x = x + 1
   print 'x =', x
   return x

x = 3
z = f(x)
# x = 4
print 'z =', z
# z = 4
print 'x =', x
# x = 3
```

1. The *formal* parameter `x` is **bound** to the value of the *actual* parameter `x`
2. Upon entry of a function, a new **scope** is created
    - A scope is mapping from names to objects

**Assert** - a command in which the the keyword assert is followed by an expression that evaluates to `True` or `False`.  
* `True` - nothing happens
* `False` - the program stops with an `AssertionError`

**Defensive programming** - assert allows for a safety switch, that possibly tests the input against what's expected and if the expectations are met, continue, or else just exit out of the program, because it is not capable of dealing with this input.

##Scope##

This is what the interpreteer creates at first, it grabs all the `def`s and in so doing will build the scope.

```Python
def f1(x):
   def g():
       x = 'abc'
       assert False
   x = x + 1
   print 'x =', x
   g()
   
   return x

x = 3
z = f1(x)
```

Main scope  
1. In outer most scope it will take `F1` and see that it maps to some code, then it stops.
2. Second is `x` and maps it to an `integer` object `3`
3. Finally it creates an object `z`, but before assigning it a value, it first invokes the function `f1()`. Now the interpreter executes the `f1`
    - F1 scope  
        - g 
        - x = 3
            - g scope

All scopes are eventually retired when they finish executing, so `g` scope is the first one to go, then `f1`.

##Debugging##

**stack viewer** - displays the stack frames. Last in, first out - a stack in computing.

Scalar types
________________

Up till now everything has been a numeric programs. *Strings* have been the first *non-scalar* object types. Also add to the list *tuples*.

**Slicing** - creates a new object from a string or other non-scalar type.
