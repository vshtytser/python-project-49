from random import randint

number_of_rounds = 3


def welcome_user():
    print("Welcome to the Brain Games!")


def get_user_name():
    user_name = input("May I have your name? ")
    return user_name


def greet_user(user_name):
    print(f"Hello, {user_name}!")


def announce_task(task):
    print(task)


def generate_random_int():
    random_number = randint(1, 100)
    return random_number


def ask_question(question_content):
    print(f"Question: {question_content}")


def user_answer_input():
    user_answer = input("Your answer: ")
    return user_answer


def check_answer(user_answer, solution):
    return user_answer == solution


def congratulate_user_round():
    print("Correct!")


def congratulate_user_game(user_name):
    print(f"Congratulations, {user_name}!")


def show_correct_answer(user_answer, solution):
    print(
        f"'{user_answer}' is wrong answer ;(. Correct answer was '{solution}'.")


def invite_back(user_name):
    print(f"Let's try again, {user_name}!")
