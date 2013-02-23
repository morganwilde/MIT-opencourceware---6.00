Machine interpretation of a program
===================================

The bisection search problem from last lecture (does it work for all inputs?).

```Python
x = 0.5
epsilon = 0.01
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print 'ans =', ans, 'low =', low, 'high =', high
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ans, 'is close to square root of', x
```

Most common problem in debugging programms is that people are lazy, I.e. not designing the test appropriatelly.
