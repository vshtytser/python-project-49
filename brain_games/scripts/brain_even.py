from random import randint

positive_answer = 'yes'
negative_answer = 'no'


def announce_task():
    print(
        f'Answer "{positive_answer}" if the number is even, otherwise answer "{negative_answer}".')


def generate_random_int():
    return randint(0, 100)


def is_even(integer):
    return integer % 2 == 0


def play_game():
    rounds = 3
    round_success_phrase = 'Correct!'

    while rounds != 0:
        rounds -= 1
        round_random_int = generate_random_int()
        round_solution = is_even(round_random_int)

        print(f'Question: {round_random_int}')
        user_answer = input('Your answer: ')

        if round_solution:
            if user_answer == positive_answer:
                print(round_success_phrase)
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. Correct answer was '{positive_answer}'.")
                break

        else:
            if user_answer == negative_answer:
                print(round_success_phrase)
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. Correct answer was '{negative_answer}'.")
                break

    if rounds == 0:
        print('Congratulations, Bill!')
    else:
        print("Let's try again, Bill!")


announce_task()
play_game()
