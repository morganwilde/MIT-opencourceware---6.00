## Helpers
def floatIn(prompt):
    """Provide a string to act as prompt"""
    return float(raw_input(prompt + ': '))
def money(floatValue):
    """Takes a float and rounds it to two decimal positions"""
    rounded = round(floatValue, 2)
    formated = '$%0.02f' % rounded
    return str(formated)

## Problem 1

# User input
outstandingBalance = floatIn('Enter the outstanding balance on your credit card')
annualRate = floatIn('Enter the annual credit card interest rate as a decimal')
minMonthlyRate = floatIn('Enter the minimum monthly payment rate as a decimal')

monthNow = 1
totalPaid = 0.0

for monthNow in range(1, 13):
    # Calculate the current month
    minMonthlyPayment   = outstandingBalance * minMonthlyRate
    interestPaid        = outstandingBalance * (annualRate / 12.0)

    principalPaid       = minMonthlyPayment - interestPaid
    totalPaid          += minMonthlyPayment
    outstandingBalance -= principalPaid

    # Return the results for this month
    print 'Month '                      + str(monthNow)
    print 'Minimum monthly payment: '   + money(minMonthlyPayment)
    print 'Principle paid: '            + money(principalPaid)
    print 'Remaining balance: '         + money(outstandingBalance)

# Print out the final result
print 'RESULT'
print 'Total amount paid: ' + money(totalPaid)
print 'Remaining balance: ' + money(outstandingBalance)

## Problem 2

# User input
outstandingBalance = floatIn('Enter the outstanding balance on your credit card')
annualRate = floatIn('Enter the annual credit card interest rate as a decimal')

memBalance  = outstandingBalance # after a loop reset balance to the input one
monthlyRate = annualRate / 12.0
monthNow    = 1
minMonthPay = 10

while outstandingBalance > 0:
    # loop to see if the min. monthly payment will do
    for monthNow in range(1, 13):
        if outstandingBalance > 0:
            interestPaid        = outstandingBalance * monthlyRate
            principalPaid       = minMonthPay - interestPaid
            outstandingBalance -= principalPaid

            if outstandingBalance <= 0:
                break

    # after the loop check if it did
    if outstandingBalance > 0:
        # if the payment is not enough, increase it by 10 and reset the balance
        outstandingBalance = memBalance
        minMonthPay += 10
    else:
        print 'RESULT'
        print 'Monthly payment to pay off debt in 1 year:', money(minMonthPay)
        print 'Number of months needed:', monthNow
        print 'Balance:', money(outstandingBalance)

## Problem 3

# User input
outstandingBalance = floatIn('Enter the outstanding balance on your credit card')
annualRate = floatIn('Enter the annual credit card interest rate as a decimal')

# calculate the lower and upper bounds for min. monthly payment
minMonthPayLower = round(outstandingBalance / 12.0, 2)
minMonthPayUpper = round((outstandingBalance * (1 + (annualRate / 12.0)) ** 12) / 12.0, 2)

# abstract the guessing
def guessCheck(balance, rate, payment):
    monthNow = 1
    for monthNow in range(1, 13):
        if balance > 0:
            interestPaid = balance * (rate / 12.0)
            principalPaid = payment - interestPaid
            balance -= principalPaid

            if balance <= 0:
                break
    return dict({'balance': balance, 'months': monthNow})

epsilon = 0.01
guess   = (minMonthPayLower + minMonthPayUpper) / 2.0
iterations = 0

# run this while the balance remains above or equal to epsilon (0.01 this case)
while abs(guessCheck(outstandingBalance, annualRate, guess)['balance']) >= epsilon and iterations < 10**6:
    # safety net
    iterations += 1
    
    # find the section that contains the answer
    guessChecked = guessCheck(outstandingBalance, annualRate, guess)['balance']
    if guessChecked < 0:
        # if guessChecked is less than 0, that means outstanding balance has been paid by then, \
        # thus this becomes the upper bound for the next guess
        minMonthPayUpper = guess
    elif guessChecked == 0:
        # a good enough guess
        break
    else:
        # if it more than 0, the answer remains between this point and the upper bound
        minMonthPayLower = guess
    # make a new guess within that section
    guess = (minMonthPayLower + minMonthPayUpper) / 2.0

findings = guessCheck(outstandingBalance, annualRate, guess)
print 'RESULT (in ' + str(iterations) + ' iterations)'
print 'Monthly payment to pay off debt in 1 year:', money(guess)
print 'Number of months needed:', findings['months']
print 'Balance:', money(findings['balance'])
