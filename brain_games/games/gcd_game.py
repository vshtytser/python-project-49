task = "Find the greatest common divisor of given numbers."


def find_whole_dividers(int):
    dividers = []

    for div in range(1, int + 1):
        if int % div == 0:
            dividers.append(div)
    return dividers


def find_common_dividers(list_1, list_2):
    common_dividers = []

    for div in list_1:
        if div in list_2:
            common_dividers.append(div)
    return common_dividers


def find_largest_common_divider(list):
    largest_common_divider = max(list)
    return largest_common_divider
