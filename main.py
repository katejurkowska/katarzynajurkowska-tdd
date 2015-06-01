def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def fib_numbers():
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b


def sum_limit(numbers, limit):
    current_sum = 0
    for number in numbers:
        if current_sum + number > limit:
            break
        else:
            current_sum += number
    return current_sum
