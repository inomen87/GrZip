def even_odd(numlist, oddoreven):
    if isinstance(numlist, list):
        if isinstance(oddoreven, str):
            oddlist = []
            evenlist = []
            if oddoreven == "odd":
                for element in numlist:
                    if isinstance(element, int):
                        if element % 2 != 0:
                            oddlist.append(element)
                return oddlist
            elif oddoreven == "even":
                for element in numlist:
                    if isinstance(element, int):
                        if element % 2 == 0:
                            evenlist.append(element)
                return evenlist
        else:
            return None
    else:
        return None






def addition(numlist):
    """ 1. can use type(int) instead of isinstance
     2. use not isinstance and return None at the start of the function
     3. homework: make function work with integer, float and complex
     4. instead of return None try to raise an error message"""
    if isinstance(numlist, list):
        totalsum = 0
        for num in range(len(numlist)):
            if isinstance(numlist[num], int):
                totalsum += numlist[num]
        return totalsum
    else:
        return None







def difference(numlist):
    """1.  make it work with float and complex
    2. rewrite it with enumerate"""
    if isinstance(numlist, list):
        totalsum = 0
        for element in numlist:
            if isinstance(element, int):
                totalsum += element
        return totalsum
    else:
        return None







def multiplication(numlist):
    """
     1. write while loop starting from zero up and don't use pop method
     2. change isinstance to type(int) and make it negative so it returns None at the beginning of function"""
    if isinstance(numlist, list):
        counter = len(numlist)
        result = 1
        while counter >= 1: # if we want an infinite loop we can use: "while 1:"
            if isinstance(numlist[0], int):
                result *= numlist[0]
            numlist.pop(0)
            counter -= 1
        return result
    else:
        return None






def division(numlist):
    if isinstance(numlist, list) and len(numlist) > 1:
        divisor = 1
        counter = 0
        for element in numlist:
            if counter == 0:
                divisor = element / divisor
                counter += 1
            else:
                divisor = divisor / element
        return divisor
    else:
        raise ValueError


if __name__ == "__main__":
    print(even_odd([6, "o", 7, 8], "even"))
    print(addition([6, "i", 8]))
    print(difference([6, "7,3,4,5,6,7", 8]))
    print(multiplication([0, "2,3,4,5,6,7,8", 9]))
    print(division([1, 2, 3, 4, 5, 6, 7, 8, 9]))

