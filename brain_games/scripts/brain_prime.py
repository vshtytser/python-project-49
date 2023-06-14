#!/usr/bin/env python3
from brain_games.games import general_games
from brain_games.games import prime_game


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)
    general_games.announce_task(prime_game.task)

    while general_games.number_of_rounds != 0:
        question_content = general_games.generate_random_int()
        general_games.ask_question(question_content)

        solution = prime_game.check_if_number_prime(question_content)
        # print(f"***test_solution: {solution}")

        user_answer = general_games.user_answer_input()

        if prime_game.check_if_number_prime(question_content) is True:
            solution = prime_game.positive_answer
        else:
            solution = prime_game.negative_answer

        if general_games.check_answer(user_answer, solution) is True:
            general_games.congratulate_user_round()
            general_games.number_of_rounds -= 1
        else:
            general_games.show_correct_answer(user_answer, solution)
            break

    if general_games.number_of_rounds == 0:
        general_games.congratulate_user_game(user_name)
    else:
        general_games.invite_back(user_name)


if __name__ == '__main__':
    main()
