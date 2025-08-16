import random

def game():
    # Introduction and instructions for the player
    print("Welcome to the number guessing game, I am thinking of a number you have to guess it correctly in certain number of attempts: ")
    print("You have the choice to choose between easy and hard level. ")
    print("Easy level will give you 10 attempts and in hard you will have 5. ")

    while True: 
        # Ask the player to choose difficulty level
        choose = input("Enter your choice easy or hard. (E/H)").upper()

        # Easy mode logic
        if choose == 'E':
            attempts = 10  # set number of attempts for easy mode
            computer_choice = random.randint(1,100)  # generate random number between 1 and 100
            
            while True:
                easy_choice = int(input("Guess the correct number: "))

                # If the guess matches the random number
                if easy_choice == computer_choice:
                    print(f"Number guessed correctly in attempts {attempts - 1} left")
                    break  # stop the game once guessed correctly

                # Reduce attempts after a wrong guess
                attempts -=1

                # Give hints based on the guess
                if easy_choice > computer_choice:
                    print(f"Too high, {attempts} left")
                elif easy_choice < computer_choice:
                    print(f"Too low, {attempts} left")    

                # End game if no attempts left
                if attempts == 0:
                    print("No more attempts left")
                    break

        # Hard mode logic
        if choose == 'H':
            attempts = 5  # set number of attempts for hard mode
            computer_choice = random.randint(1,100)  # generate random number between 1 and 100

            while True:
                hard_choice = int(input("Guess the correct number: "))

                # If the guess matches the random number
                if hard_choice == computer_choice:
                    print(f"Number guessed correctly in attempts {attempts - 1} left")
                    break  # stop the game once guessed correctly

                # Reduce attempts after a wrong guess
                attempts -=1

                # Give hints based on the guess
                if hard_choice > computer_choice:
                    print(f"Too high, {attempts} left")
                elif hard_choice < computer_choice:
                    print(f"Too low, {attempts} left")    

                # End game if no attempts left
                if attempts == 0:
                    print("No more attempts left")
                    break       

game()
