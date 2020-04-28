import sys
import random

class GuessTheNumber:
    
    def guess():
        num = random.randint(1,100)
        print("How many attempts would you like to have:")
        attempts = int(input())
        for i in range(attempts):
            try:
                guessed_num = int(input('Enter your guess (in between 1 and 100) : '))
            except:
                print('Enter a valid integer')
            if guessed_num == num:
                print("Congrats!! You've guessed the correct number",num)
                break
            elif guessed_num>100 or guessed_num<0:
                print('The number is in between 1 and 100')
            elif guessed_num>num:
                print('Your guess is too big. Try Again')
            elif guessed_num<num:
                print('Your guess is too small. Try again')
            if attempts==0:
                print('YOU LOST')
            else: print('Remaining Attempts:', attempts-i-1)
            
    def start():
        print("""The system will generate a random number between 1 to 100.
        Guess the number correctly to win the game.""")
        while(1):
            print('Press Y to start the game OR enter to quit')
            n = input()
            if n=='Y' or n=='y':
                GuessTheNumber.guess()
            else:
                print('Good Bye.')
                sys.exit()

GuessTheNumber.start()
