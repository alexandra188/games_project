#!/usr/bin/env python
import random


def welcome_user():
    """Welcome user and get name."""
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_progression():
    """Generate arithmetic progression with one missing element."""
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    
    # Создаём прогрессию
    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(str(current_element))
    
    # Прячем один элемент
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    
    return ' '.join(progression), correct_answer


def play_game():
    """Main game logic for Progression game."""
    name = welcome_user()
    print("What number is missing in the progression?")

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_progression()
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
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
