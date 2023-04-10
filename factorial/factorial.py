def factorial(n):
    # Global variables are to be avoided whenever possible. Here it is possible to avoid globals.
    # Read https://docs.python.org/3.8/reference/simple_stmts.html#the-global-statement for the global statement.
    # Easy read about Variables and Scope: https://www.geeksforgeeks.org/python-scope-of-variables/
    # TODO: Think about how to rewrite the function without globals, or any variable other than the parameter n
    global counter_1
    global counter_2
    global counter_3

    while counter_2 < control_num:
        n = n * counter_1
        counter_1 += 1
        counter_2 += 1

        factorial(n) # TODO: You are not handling the return of this recursive call !

    if counter_3 == 1:

        counter_3 += 1
        return n
    # TODO: The function does not return the value of factorial(n) A function that does not return anything is bad
    #  code style in general

def factorial_recursive(n):
    """DOC STRING"""
    pass

def factorial_loop(n):
    """DOC STRING"""
    pass

if __name__ == '__main__':
    input_num = int(input("Type the number: "))  # TODO: Please move this to main clause. Anything that is only executed when the file is called via python factorial.py has to go into the __main__ part.
    control_num = input_num - 2
    counter_1 = 2
    counter_2 = 0
    counter_3 = 1
    factorial(input_num)
