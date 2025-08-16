#  Blackjack Game in Python

This project is a simple **Blackjack (21)** game built using Python.  
It helps beginners practice **functions, loops, and conditionals** while creating an interactive game.

---

##  Rules of Blackjack

1. Both the player and the computer (dealer) start with **two cards**.
2. The goal is to get as close to **21** as possible without going over.
3. Number cards (2–10) are worth their face value.
4. Face cards (J, Q, K) are worth **10**.
5. **Ace (A)** can count as **11** or **1**, whichever is more favorable.
6. The player decides whether to:
   - **Hit (draw another card)**, or
   - **Stand (keep current hand)**.
7. After the player finishes, the computer plays:
   - It keeps drawing until it reaches a score of **17 or higher**.
8. Whoever is closer to **21** without going over wins.
9. If both bust (go over 21), it’s a tie.

---

##  Game Logic (Step by Step)

1. **Deal Initial Hands**  
   - Player gets two random cards.  
   - Computer gets two random cards.  

2. **Player's Turn**  
   - Show cards and ask if they want to **Hit**.  
   - If they choose **Hit**, add another card.  
   - If score > 21 but an **Ace** is present, convert Ace from 11 → 1.  

3. **Computer's Turn**  
   - Computer keeps drawing until its score is **≥ 17**.  

4. **Compare Scores**  
   - Check conditions:
     - Busts (score > 21).  
     - Closest to 21 wins.  
     - Equal scores → Draw.  

5. **How to Run**

    - Save the code as blackjack.py.

    - Run in terminal/command prompt:

    - python blackjack.py


    - Follow on-screen instructions and enjoy! 