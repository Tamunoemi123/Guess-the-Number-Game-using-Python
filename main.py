import random

# Keep track of attempts
attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def start_game():
    random_number = random.randint(1, 10)
    print("Hey there! Welcome to the game of guesses!")
    player_name = input("Enter your name: ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No): ".format(player_name))

    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range")

            attempts += 1

            if guess == random_number:
                print("Congrats! You guessed it right!")
                print("It took you {} attempts".format(attempts))
                attempts_list.append(attempts)

                play_again = input("Would you like to play again? (Enter Yes/No): ")

                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
                else:
                    attempts = 0
                    random_number = random.randint(1, 10)
                    show_score()
            elif guess < random_number:
                print("It's higher!")
            else:
                print("It's lower!")

        except ValueError as err:
            print("Oh!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a nice day!")

if __name__ == '__main__':
    start_game()
