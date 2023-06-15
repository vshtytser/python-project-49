positive_answer = "yes"
negative_answer = "no"

task = f'Answer "{positive_answer}" if given number is prime. Otherwise answer "{negative_answer}".'


def check_if_number_prime(number):
    divisors = []
    for num in range(2, number):
        if number % num == 0:
            divisors.append(num)
    return len(divisors) == 0
