annualInterestRate = .2

balance = 320000

monthlyInterestRate = annualInterestRate/12

balanceCopy = balance

minPay = balanceCopy / 12

maxPay = (balanceCopy * (1 + monthlyInterestRate) ** 12) / 12

pay = (minPay + maxPay) / 2

while True:
    for i in range(12):
        monthlyUnpaid = balance - pay
        balance = monthlyUnpaid + monthlyInterestRate * monthlyUnpaid
    if balance >= 1:
        balance = balanceCopy
        minPay = pay
        pay = (minPay + maxPay) / 2
    elif balance <= -1:
        balance = balanceCopy
        maxPay = pay
        pay = (minPay + maxPay) / 2
    else:
        break
print("Lowest Payment: " + str(round(pay,2)))