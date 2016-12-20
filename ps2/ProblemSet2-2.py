annualInterestRate = .12
balance = 6000

monthlyInterestRate = annualInterestRate/12
minPay = 0

balanceCopy = balance
while balance > 0:
    balance = balanceCopy
    minPay += 10
    for i in range(12):
        monthlyUnpaid = balance - minPay
        balance = monthlyUnpaid + monthlyInterestRate * monthlyUnpaid
print("Lowest Payment: " + str(round(minPay,2)))