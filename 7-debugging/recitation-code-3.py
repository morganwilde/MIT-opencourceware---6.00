#
# Multiplication (pretend no * operator available)
#
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
