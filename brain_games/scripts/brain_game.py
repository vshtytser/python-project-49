#!/usr/bin/env python3
from brain_games.games import general_games


def main():
    general_games.welcome_user()
    user_name = general_games.get_user_name()
    general_games.greet_user(user_name)


if __name__ == '__main__':
    main()
