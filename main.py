from random import randint

chosen_number = randint(1,101)
guess_total = 0
guess_list = []
last_guess = 0
correct_guess = False

print('Welcome to The Guessing Game\nThe Program has picked a random number\nAnd you must guess what that number is')
print('the number is between 1 and 100, so you must chose a number in this range')
print('After your first guess, if you are within 10 numbers of the desired number, you will see "Warm"')
print('Otherwise you will see "Cold", in the subsequent guesses, if you are closer to the number, you will see "Warmer!"')
print('Otherwise you will see "Colder", Finaly when you guess the number, the program will tell how many tries it took')

while correct_guess == False:
    last_guess = int(input('What number do you pick?'))
    if 0 >= last_guess or last_guess >= 101:
        print('You are out of range! pick again.')
        guess_total += 1
        continue
    elif last_guess == chosen_number:
        print(f'You have chosen correctly! it took you {guess_total} tries to do so.')
        correct_guess = True
    else:
        if guess_total == 0:
            if abs(chosen_number-last_guess) < 11:
                print('Warm')
                guess_list.append(last_guess)
                guess_total += 1
            else:
                print('Cold')
                guess_list.append(last_guess)
                guess_total += 1
        else:
            if abs(chosen_number-guess_list[-1]) > abs(chosen_number-last_guess):
                print('Warmer!')
                guess_list.append(last_guess)
                guess_total += 1
            else:
                print('Colder!')
                guess_list.append(last_guess)
                guess_total += 1