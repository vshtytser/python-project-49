positive_answer = "yes"
negative_answer = "no"

task = f'Answer "{positive_answer}" if the number is even, otherwise answer "{negative_answer}".'


def check_if_even(integer):
    return integer % 2 == 0
