import random

# Load high score from file
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

def game():
    # List of celebrities with follower counts
    data = [
        {"name": "Cristiano Ronaldo", "country": "Portugal", "follower_count": 630},
        {"name": "Selena Gomez", "country": "USA", "follower_count": 430},
        {"name": "Virat Kohli", "country": "India", "follower_count": 270},
        {"name": "Lionel Messi", "country": "Argentina", "follower_count": 520},
        {"name": "Kylie Jenner", "country": "USA", "follower_count": 400},
        {"name": "Dwayne Johnson", "country": "USA", "follower_count": 390},
        {"name": "Ariana Grande", "country": "USA", "follower_count": 380},
        {"name": "Kim Kardashian", "country": "USA", "follower_count": 360},
        {"name": "Beyoncé", "country": "USA", "follower_count": 320},
        {"name": "Taylor Swift", "country": "USA", "follower_count": 310}
    ]

    score = 0

    while True:
        # Pick 2 random celebrities
        a, b = random.sample(data, 2)

        # Ask user
        choice = input(f"Who has more followers {a['name']} or {b['name']}? Pick A or B: ").strip().lower()

        # Check answer
        if (choice == 'a' and a['follower_count'] > b['follower_count']) or \
           (choice == 'b' and b['follower_count'] > a['follower_count']):
            score += 1
            print(f"Correct! Your score is {score}")
        else:
            print(f"Wrong! Your final score is {score}")

            # Check for high score and update file if beaten
            global high_score
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as file:
                    file.write(str(high_score))
                print(f"🎉 New High Score: {high_score}")
            else:
                print(f"High Score remains: {high_score}")
            break  # end current session

# Main loop for replay
while True:
    game()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
