
import random

def guess_game(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print('Guessing Matched!!')
            return True
    else:
        print('hey bozo, I said 1 to 10!!?')
        return False

if __name__ == '__main__' :
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number between 1-10:  '))
            if(guess_game(guess,answer)):
                break

        except(ValueError,TypeError):
            print('Please enter a number')
            continue
