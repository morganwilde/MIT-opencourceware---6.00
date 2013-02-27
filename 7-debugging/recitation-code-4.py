#
# Multiplication (pretend no * operator available)
#
# recursive function
def rec_mult(m, n):
    # Base case (only occur if call the function
    if n == 0:
        return 0
    elif n >= 1:
        return m + rec_mult(m, n-1)
    elif n <= -1:
        return -m + rec_mult(m, n+1)
# Test! Remember test cases should always test ALL inputs, and be tests that you KNOW the correct answer
print 'Recursive multiplication tests:'
print rec_mult(8, 0) # 0
print rec_mult(3, 4) # 12
print rec_mult(-3, 4) # -12
print rec_mult(3, -4) # -12
print rec_mult(-3, -4) # 12

# iterative function
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
# Test it
print 'Iterative multiplication tests:'
print iter_mult(8, 0) # 0
print iter_mult(3, 4) # 12
print iter_mult(-3, 4) # -12
print iter_mult(3, -4) # -12
print iter_mult(-3, -4) # 12

#
# Fibonacci
#
# recursive version
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
# Test
print 'Recursive fibonacci'
print rec_fib(1)
print rec_fib(2)
print rec_fib(3)
print rec_fib(4)
print rec_fib(5)

# iterative version
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
# Test
print 'Iterative fibonacci'
print iter_fib(1)
print iter_fib(2)
print iter_fib(3)
print iter_fib(4)
print iter_fib(5)

#
# Bisection search
#
# recursive version
def rec_bisection_sqrt(x, epsilon=0.01, low=None, high=None):
    '''
    Performs a recursive bisection search to find the
    square root of x, within epsilon
    '''
    if low == None:
        low = 0.0
    if high == None:
        high = x
    midpoint = (low+high) / 2.0
    # if the difference of the midpoint squared and x is
    # within the epsilon tolerance, OR if the midpoint is greater
    # than x, we stop and give an answer
    if abs(midpoint**2-x) < epsilon or midpoint > x:
        return midpoint
    else:
        # Otherwise, check if the midpoint is too big or small
        if midpoint**2 < x:
            # If too small, recurse on upper half or range
            return rec_bisection_sqrt(x, epsilon=0.01, midpoint, high)
        else:
            # If too big, recurse on lower half of range
            return rec_bisection_sqrt(x, epsilon=0.01, ,low midpoint)

# iterative version
def iter_bisection_sqrt(x, epsilon=0.01):
    '''
    '''
    low = 0.0
    high = x
    midpoint = (high+low) / 2.0
    # loop until the difference of the midpoint is
    # withing the epsilon tolerance, OR until
    while abs(midpoint**2 - x) >= epsilon and midpoint < x:
        # Check if the midpoint of the range is lower than x
        if midpoint**2 < x:
            # If too small, set new lower bound
            low = midpoint
        else:
            # If too big, set new upper bound
            high = midpoint
        # Recalculate the midpoint
        midpoint = (high+low)/2.0
    return midpoint
