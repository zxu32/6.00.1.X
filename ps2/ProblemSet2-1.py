balance = 5000

annualInterestRate = .12

monthlyPaymentRate = .1

balanceCopy = balance

totalPaid = 0

for i in range(1,13):
    monthlyPayment = balanceCopy * monthlyPaymentRate
    balanceCopy = balanceCopy + balanceCopy*annualInterestRate/12 - monthlyPayment
    totalPaid += monthlyPayment
    print('Month: ', i)
    print('Minimum monthly payment: ', round(monthlyPaymentRate * balanceCopy, 2))
    print('Remaining balance: ', round(balanceCopy, 2))

print('Total paid: ', round(totalPaid, 2))