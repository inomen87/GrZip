
input_num = int(input("type"))

counter_1 = 2
counter_2 = 0
counter_3 = 1
counter_4 = input_num - 2


def factorial(n):
    global counter_1
    global counter_2
    global counter_3

    while counter_2 < counter_4:
        n = n * counter_1
        counter_1 += 1
        counter_2 += 1

        factorial(n)

    if counter_3 == 1:
        print(n)
        counter_3 += 1


if __name__ == '__main__':
    factorial(input_num)
