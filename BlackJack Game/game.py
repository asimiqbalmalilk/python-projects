import random
def calculate_score(hand):
    # Function to calculate total score
    score = sum(hand)
    # Handling case with ace card value
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def blackjack():
    while True:
        # A list of cards having faces, aces and normal cards values
        cards = [2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 11]

        user_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards) , random.choice(cards)]

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # We print user's current score and computer's first hand pick initially
        print(f"User's choice is {user_cards} and user's total score is {user_score}")
        print(f"Computer's first hand is {computer_cards[0]}")

        # Giving choice to user to stand or go for an other pick

        hs = input("Do you want to hit or stand (h/s): ").lower()
        if hs == 'h':
            user_cards.append(random.choice(cards))
            user_score = calculate_score(user_cards)
        # Computer picks up a card if it's score is less than 17
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)

        # Displaying scores of both the players and than comparing
        print(f"Your choice's are {user_cards} and your current score is {user_score}")
        print(f"Computer's choice's are {computer_cards} and computer's current score is {computer_score}")

        if user_score > 21:
            print("Your score is greater than 21. Busted. Computer Wins")        
        elif computer_score > 21:
            print("Computer's score is greater than 21. Busted. You win")    
        elif user_score > computer_score:
            print("Your score is greater than computer's score")
        elif computer_score > user_score:
            print("Computer's score is greater than user's score")
        else:
            print("Draw")    

        # Allowing another round for increased functionality
        play_again = input("Do you want to play again (Y/N).").lower()
        if play_again == 'n':
            print("Thankyou for your time, have a nice day.")
            break
        elif play_again == 'y':
            continue
        else:
            print("Invalid input. Please try again")
blackjack()            