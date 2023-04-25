


from .array_math_01 import even_odd, addition, multiplication, difference


cases_even = (
    (([6, "o", 7, 8], "even"), [6, 8]),
    (([6, 2, 5, 7 ,8], "even"), [6, 2, 8]),
)


cases_odd = (
    (([6, 1, 3, 4, 8], "odd"), [1, 3]),
)



cases_addition = (
    ([6,"i",8], 14),
    ([6,1,2,8], 17),
    ([6,-2,3,8], 15),
)

cases_multiplication = (
    ([2,"2,3,4,5,6,7,8",9], 18),
    ([2,3,4], 24),
    ([2,-10,3], -60),
)

cases_difference = (
    ([2,"2,3,4,5,6,7,8",9], 11),
    ([2,1,3,9], 15),
    ([2,5,2,1,9], 19),
)



def test_even_odd():
    for case in cases_even:
        assert even_odd(case[0][0], "even") == case[1]
    for case in cases_odd:
        assert even_odd(case[0][0], "odd") == case[1]


def test_addition():
    for case in cases_addition:
        assert addition(case[0]) == case[1]


def test_multiplication():
    for case in cases_multiplication:
        assert multiplication(case[0]) == case[1]


def test_difference():
    for case in cases_difference:
        assert difference(case[0]) == case[1]