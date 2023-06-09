from random import choice

task = "What is the result of the expression?"


def generate_random_operator():
    operators = ["+", "-", "*"]
    random_operator = choice(operators)
    return random_operator


def calculate_solution(random_int_1, random_int_2, random_operator):
    if random_operator == '+':
        solution = random_int_1 + random_int_2
    elif random_operator == '-':
        solution = random_int_1 - random_int_2
    elif random_operator == '*':
        solution = random_int_1 * random_int_2
    return solution
