#!/usr/bin/env python
import random


def welcome_user():
    """Welcome user and get name."""
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_prime(n):
    """Check if number is prime without using libraries."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Проверяем делители до квадратного корня из n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def play_game():
    """Main game logic for Prime game."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 50)
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        
        correct_answer = 'yes' if is_prime(number) else 'no'
        
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
