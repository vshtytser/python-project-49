from random import randint

task = "What number is missing in the progression?"
min_progression_length = 5
max_progression_length = 10
game_placeholder = ".."


def generate_progression_length():
    progression_length = randint(min_progression_length, max_progression_length)
    return progression_length


def generate_progression(start_number, progression_step, progression_length):
    progression = [start_number]
    for num in range(progression_length - 1):
        progression.append(progression[num] + progression_step)
    return progression


def generate_random_index(progression_length):
    random_index = randint(0, progression_length - 1)
    return random_index


def convert_list_to_str(list):
    string = ""
    for value in list:
        string += f"{value} "
    return string.strip()
