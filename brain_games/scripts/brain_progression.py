#!/usr/bin/env python3
from brain_games.games import general_games
from brain_games.games import progression_game


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)
    general_games.announce_task(progression_game.task)

    while general_games.number_of_rounds != 0:
        start_number = general_games.generate_random_int()
        progression_step = general_games.generate_random_int()
        progression_length = progression_game.generate_progression_length()

        progression_list = progression_game.generate_progression(
            start_number, progression_step, progression_length)

        hidden_num_index = progression_game.generate_random_index(
            progression_length)
        hidden_num = progression_list[hidden_num_index]
        solution = hidden_num

        game_list = progression_list
        game_list[hidden_num_index] = progression_game.game_placeholder

        question_content = progression_game.convert_list_to_str(game_list)
        general_games.ask_question(question_content)

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
