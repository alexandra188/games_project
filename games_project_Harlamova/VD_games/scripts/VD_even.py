import random
from ..cli import welcome_user


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def play_game():
    """Main game logic."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        # Проверка на корректный ввод (только yes или no)
        if answer not in ["yes", "no"]:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if is_even(number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Entry point."""
    play_game()


if __name__ == "__main__":
    main()
