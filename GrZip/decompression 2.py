def decompress(inputstring):
    """ Function decompresses an input string which is a compressed alphanumeric string. Input string comes
    in the following format e.g.: "(4),(X),(5),(c)". In this example 4 and 5 are compression values and X and c are
    compressed alphanumeric characters. ( and ) are just delimiters. The function then returns a decompressed
    string in this format: "XXXXccccc". """
    # In first_list we split the input string at commas
    first_list = inputstring.split(",")
    second_list = []
    # We use replace() method to get rid of parenthesis in our compressed string and save result in a list
    for index in first_list:
        second_list.append(index.replace("(", "").replace(")", ""))

    print(second_list)

    for num in range(len(second_list)):
        # Now thanks to modulo we know that every number that indicates compression level is going to be even
        if second_list.index(second_list[num]) % 2 == 0:
            num_char = int(second_list[num]) - 1    # We take that compression level number and turn it into integer
            # We insert alphanumeric characters instead of numbers in the right position
            second_list.insert(num, second_list[num + 1] * num_char)
            second_list.pop(num + 1)

    second_list = "".join(second_list)  # Finally we will join a list into a string again and print it out
    return second_list

print(decompress("(58,X),(666,c),(455,b),(58,B),(666,R),(455,5)"))

