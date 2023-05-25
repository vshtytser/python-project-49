from random import randint
from random import choice


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


def generate_random_operator():
    operators = ["+", "-", "*"]
    random_operator = choice(operators)
    return random_operator


random_int_1 = generate_random_int()
random_int_2 = generate_random_int()
random_operator = generate_random_operator()


def ask_question(random_int_1, random_int_2, random_operator):
    print(f"Question: {random_int_1} {random_operator} {random_int_2}")


def calculate_solution(random_int_1, random_int_2, random_operator):
    # print(f"{random_int_1} {random_operator} {random_int_2}")
    solution = eval(f"{random_int_1} {random_operator} {random_int_2}")
    return solution
# print(check_solution(random_int_1, random_int_2, random_operator))


def check_answer(user_answer, solution):
    return user_answer == solution


def congratulate_user_round():
    print("Correct!")


def congratulate_user_game(user_name):
    print(f"Congratulations, {user_name}!")


def tell_correct_answer(user_answer, solution):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{solution}'.")


def invite_back(user_name):
    print(f"Let's try again, {user_name}!")
