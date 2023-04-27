"""
Test Cases for array math
"""

# from .array_math import addition as add
# from .array_math import difference as subtract
# from .array_math import multiplication as multiply
# from .array_math import even_odd

from .array_math_01 import even_odd, addition as add, multiplication as multiply, difference as subtract

addition_testcases = (
    ([],None),
    ([1],None),
    ([1,2],3),
    ([1,2,3],6),
    ([1,"hello",2,3,"world"],6),
    ([1,list("123"),2,3,dict()],6),
    ([84,831,389,981,22],2307),
)

def test_array_math_addition():
    for case in addition_testcases:
        assert add(case[0]) == case[1], "Bad addition of array. Return value wrong"

subtraction_testcases = (
    ([],None),
    ([1],None),
    ([1,2],-3),
    ([1,2,3],-6),
    ([1,"hello",2,3,"world"],-6),
    ([1,list("123"),2,3,dict()],-6),
    ([84,831,389,981,22],-2307),
)

def test_array_math_subtraction():
    for case in subtraction_testcases:
        assert subtract(case[0]) == case[1], "Bad subtraction of array. Return value wrong"

multiplication_testcases = (
    ([],None),
    ([1],None),
    ([1,2],2),
    ([1,2,3],6),
    ([1,"hello",2,3,"world"],6),
    ([1,list("123"),2,3,dict()],6),
    ([84,831,389,981,22],586032361992),
)

def test_array_math_multiplication():
    for case in multiplication_testcases:
        assert multiply(case[0]) == case[1], "Bad multiplication of array. Return value wrong"

even_odd_testcases = (
    #list, even?, return
    ([], True, None),
    ([], False, None),
    ([1], True, []),
    ([1], False, [1]),
    ([1, 2], True, [2]),
    ([1, 2], False, [1]),
    ([1, 2, 3], True, [2]),
    ([1, 2, 3], False, [1, 3]),
    ([1,"hello",2,3,"world"], True, [2]),
    ([1,list("123"),2,3,dict()], False, [1, 3]),
    ([84,831,389,981,22], True, [84, 22]),
    ([84,831,389,981,22], False, [831, 389, 981]),
)

def test_array_math_even_odd():
    for case in even_odd_testcases:
        return_value = even_odd(case[0], case[1])
        print(case)
        print(return_value)
        assert return_value== case[2], "Bad even/odd in array. Return value wrong"