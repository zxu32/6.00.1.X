low = 0
high = 100
guess = (low+high)/2
print ('Please guess a secret number between 0 and 100!')
while True:
    print ('is your secret number ', guess, '?')
    feedback = input("enter 'h' to indicate the guess is too high. "\
                     "enter 'l' to indicate the guess is too low. "\
                     "enter 'c' to indicate I guessed corretly.")
    if feedback == 'h':
        high = guess
        guess = (low+high)/2
    elif feedback == 'l':
        low = guess
        guess = (low+high)/2
    elif feedback == 'c':
        print ('Game over. Your secret number was: ', guess)
        break
    else:
        print ('not correct argument.')
