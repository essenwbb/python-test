import math
import profile


def fibonacci(n):
    return int(1 / math.sqrt(5) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n))


def fibonacci2(n):
    a, b = 0, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a


def main():
    fibonacci(1474)
    fibonacci2(1474)


if __name__ == '__main__':
    profile.run('main()')
