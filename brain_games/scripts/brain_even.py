#!/usr/bin/env python3
from .. import even_game_logic


def main():
    even_game_logic.welcome_user()
    user_name = even_game_logic.get_user_name()
    even_game_logic.greet_user(user_name)
    even_game_logic.announce_task()
    even_game_logic.play_game(user_name)


if __name__ == '__main__':
    main()
