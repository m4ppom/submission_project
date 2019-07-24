# import real
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '0으로 나눌 수 없음'


# print(div(1, 2))

# print(div(1, 0))
# print(__name__)  # __main__

if __name__ == '__main__':
    print(add(1, 2))
    print(div(1, 0))