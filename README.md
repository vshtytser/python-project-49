## Brain Games
This project consists of 5 math games, with each game having 3 rounds. The objective is to test the player's math skills.
If the player answers correctly, they are congratulated with a "Correct!" message and proceed to the next quiz. An incorrect answer reveals the correct answer and requires starting the game from the beginning.

### brain-even
This game challenges the player to determine whether randomly generated numbers are even or odd.

### brain-calc
In this game, the player is presented with random mathematical expressions involving addition (+), subtraction (-), and multiplication (*) operations. The goal is to solve the expression and provide the correct answer.

### brain-gcd
The Greatest Common Divisor (GCD) game presents the player with two random numbers. The player must calculate and enter the greatest common divisor of these numbers. 

### brain-progression
In this game, the player is shown a series of numbers (from 5 to 10) forming an arithmetic progression, with one number replaced by two dots. The player's task is to identify the missing number in the sequence.

### brain-prime
This game quizzes the player on whether a presented number is prime or not.


[![asciicast](https://asciinema.org/a/KXgxdzO724yZNUDoDDsjr0S5R.svg)](https://asciinema.org/a/KXgxdzO724yZNUDoDDsjr0S5R)

[![asciicast](https://asciinema.org/a/590778.svg)](https://asciinema.org/a/590778)

[![asciicast](https://asciinema.org/a/FrvjJA2fJovFn0MWDwU7OarmY.svg)](https://asciinema.org/a/FrvjJA2fJovFn0MWDwU7OarmY)

[![asciicast](https://asciinema.org/a/nDXM3NLEin9hC9VQUqFJHbLqa.svg)](https://asciinema.org/a/nDXM3NLEin9hC9VQUqFJHbLqa)


### Technical requrements
**Operating System:** The project should be compatible with Windows, macOS, and Linux operating systems.

**Python:** Make sure you have Python version 3.10 or newer installed on your system.

**Poetry:** The project uses Poetry as a dependency management and packaging tool. Make sure you have Poetry installed on your system. You can install Poetry by following the instructions in the Poetry documentation (https://python-poetry.org/docs/#installation).

**Dependencies:** Once you have Poetry installed, navigate to the project directory in your terminal or command prompt and run the following command to install the project dependencies:

`poetry install`

This command will install all the necessary dependencies specified in the pyproject.toml file, including the `prompt` library and development dependencies like `flake8` for code linting.


### Hexlet tests and linter status:
[![Actions Status](https://github.com/vshtytser/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/vshtytser/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/789ac1f479666ecbeea8/maintainability)](https://codeclimate.com/github/vshtytser/python-project-49/maintainability)