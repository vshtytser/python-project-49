#!/usr/bin/env python3
from brain_games.games import general_games
from brain_games.games import gcd_game


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)
    general_games.announce_task(gcd_game.task)

    while general_games.number_of_rounds != 0:
        random_int_1 = general_games.generate_random_int()
        random_int_2 = general_games.generate_random_int()

        question_content = f"{random_int_1} {random_int_2}"
        general_games.ask_question(question_content)

        common_divs_list_1 = gcd_game.find_whole_dividers(random_int_1)
        common_divs_list_2 = gcd_game.find_whole_dividers(random_int_2)
        common_divs_list = gcd_game.find_common_dividers(
            common_divs_list_1, common_divs_list_2)
        solution = gcd_game.find_largest_common_divider(
            common_divs_list)
        print(f"***test_solution: {solution}")

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
