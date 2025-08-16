# Number Guessing Game

## Overview
This is a simple Python project where the computer randomly selects a number, and the player has to guess it within a limited number of attempts. The game provides hints whether the guess is too high or too low.

---

## Rules of the Game
1. The computer randomly chooses a number between **1 and 100**.
2. You choose a difficulty level:
   - **Easy Mode (E)** → 10 attempts
   - **Hard Mode (H)** → 5 attempts
3. Enter your guesses one by one.
4. After each guess:
   - If the guess is correct → You win!
   - If the guess is wrong → The game will hint if the number is higher or lower.
   - Attempts decrease after each incorrect guess.
5. If all attempts are used → Game over.

---

## Code Flow
1. Import `random` module to generate a random number.
2. Display game instructions and ask for difficulty level.
3. Initialize attempts based on difficulty.
4. Run a loop where the player inputs guesses:
   - Check if the guess is correct → End the game.
   - Otherwise, reduce attempts and give hints.
5. If attempts reach zero → Game over.
6. Program terminates when the player wins or loses.

---

## Requirements
- Python **3.x**

---

## Future Improvements
- Including GUI for a better interface and gameplay.
- Allow the user to set a custom range of numbers.
- Track the best score (fewest attempts) across games.

---

## Author
Developed as a beginner Python project to practice:
- Loops
- Conditional statements
- Functions
- User input handling
