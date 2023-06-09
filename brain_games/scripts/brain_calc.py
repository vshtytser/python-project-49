#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.games import general_games


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)
    general_games.announce_task(calc_game.task)

    while general_games.number_of_rounds != 0:
        random_int_1 = general_games.generate_random_int()
        random_int_2 = general_games.generate_random_int()
        random_operator = calc_game.generate_random_operator()

        question_content = f"{random_int_1} {random_operator} {random_int_2}"
        general_games.ask_question(question_content)

        solution = calc_game.calculate_solution(
            random_int_1, random_int_2, random_operator)
        # print(solution)
        user_answer = int(general_games.user_answer_input())

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
