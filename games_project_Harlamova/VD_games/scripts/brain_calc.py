#!/usr/bin/env python
import random
import operator


def welcome_user():
    """Welcome user and get name."""
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def play_game():
    """Main game logic for Calculator."""
    name = welcome_user()
    print("What is the result of the expression?")

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        op = random.choice(list(operations.keys()))

        question = f"{num1} {op} {num2}"
        correct_result = operations[op](num1, num2)

        print(f"Question: {question}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    play_game()


if __name__ == "__main__":
    main()
