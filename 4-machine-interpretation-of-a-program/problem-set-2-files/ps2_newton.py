#
# 6.00 Problem Set 2
#
# Successive Approximation
#

## Problem #1

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # input verification
    if type(poly) == tuple and (type(x) == int or type(x) == float):
        assert True
    else:
        print '"poly" type =',  type(poly), ', needed "tuple"'
        print '"x" type =',     type(x),    ', needed "int" or "float"'
        assert False
    # storage devices
    index = 0
    polyValue = 0
    for multiplier in poly:
        polyValue += multiplier * (x**index) # add it up
        index += 1 # on to the next one

    return polyValue

#### Problem #1 test
##poly = (0.0, 0.0, 5.0, 9.3, 7.0)
##x = -13
##print evaluate_poly(poly, x)

## Problem #2

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # input verification
    if len(poly) > 0:
        assert True
    else:
        print '"poly" length is <= 0, needed >0'
        assert False
    # derive a new tuple
    index = 0
    polyDerived = ()
    for multiplier in poly:
        if index != 0:
            # only add a new member if the power is != 0
            polyDerived += (multiplier*index,)
        index += 1 # on to the next power

    return polyDerived

#### Problem #2 test
##poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
##print compute_deriv(poly)

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ... 

