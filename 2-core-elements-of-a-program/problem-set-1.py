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
            interestPaid        = balance * (rate / 12.0)
            principalPaid       = payment - interestPaid
            balance -= principalPaid

            if balance <= 0:
                break
    return dict({'balance': balance, 'months': monthNow})

# loop to see c happening
for i in range(1,100):
    # take a guess
    guess = (minMonthPayLower + minMonthPayUpper) / 2.0
    
    if guessCheck(outstandingBalance, annualRate, guess)['balance'] <= 0 and \
       guessCheck(outstandingBalance, annualRate, guess)['balance'] >= -0.01:
        # the guess is acceptable
        print 'RESULT'
        print 'Monthly payment to pay off debt in 1 year:', money(guess)
        print 'Number of months needed:', guessCheck(outstandingBalance, annualRate, guess)['months']
        print 'Balance:', money(guessCheck(outstandingBalance, annualRate, guess)['balance'])
        break
    else:
        # take another guess
        if guessCheck(outstandingBalance, annualRate, minMonthPayLower)['balance'] > 0 and \
           guessCheck(outstandingBalance, annualRate, guess)['balance'] < 0:
            minMonthPayUpper = guess
        else:
            minMonthPayLower = guess

