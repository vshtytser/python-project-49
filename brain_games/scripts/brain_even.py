#!/usr/bin/env python3
from brain_games.games import general_games
from brain_games.games import even_game


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)
    general_games.announce_task(even_game.task)

    while general_games.number_of_rounds != 0:
        round_num = general_games.generate_random_int()
        general_games.ask_question(round_num)

        user_answer = general_games.user_answer_input()

        solution = ""
        if even_game.check_if_even(round_num) is True:
            solution = even_game.positive_answer
        else:
            solution = even_game.negative_answer

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
