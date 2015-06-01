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
