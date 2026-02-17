#!/usr/bin/env python
import random
import math


def welcome_user():
    """Welcome user and get name."""
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def gcd(a, b):
    """Calculate greatest common divisor."""
    return math.gcd(a, b)


def play_game():
    """Main game logic for GCD game."""
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        
        question = f"{num1} {num2}"
        correct_answer = gcd(num1, num2)
        
        print(f"Question: {question}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    play_game()


if __name__ == "__main__":
    main()
