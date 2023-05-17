from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    user_name = input('May I have your name? ')
    return user_name


def greet_user(name):
    print(f'Hello {name}!')


positive_answer = 'yes'
negative_answer = 'no'


def announce_task():
    print(
        f'Answer "{positive_answer}" if the number is even, otherwise answer "{negative_answer}".')


def generate_random_int():
    return randint(0, 100)


def is_even(integer):
    return integer % 2 == 0


def play_game(user_name):
    rounds = 3
    round_success_phrase = 'Correct!'

    while rounds != 0:
        round_random_int = generate_random_int()
        round_solution = is_even(round_random_int)

        print(f'Question: {round_random_int}')
        user_answer = input('Your answer: ')

        if round_solution:
            if user_answer == positive_answer:
                print(round_success_phrase)
                rounds -= 1
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. Correct answer was '{positive_answer}'.")
                break

        else:
            if user_answer == negative_answer:
                print(round_success_phrase)
                rounds -= 1
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. Correct answer was '{negative_answer}'.")
                break

    if rounds == 0:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")
