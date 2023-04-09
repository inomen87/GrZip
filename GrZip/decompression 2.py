def decompress(inputstring):
    # In first_list we split the input string at commas
    first_list = inputstring.split(",")
    second_list = []

    for index in first_list:
        second_list.append(index.replace("(", "").replace(")", ""))

    final_list = second_list
    print(final_list)

    for num in range(len(final_list)):
        # Now thanks to modulo we know that every number that indicates compression level is going to be even
        if final_list.index(final_list[num]) % 2 == 0:
            num_char = int(final_list[num]) - 1    # We take that compression level number and turn it into integer
            # We insert alphanumeric characters instead of numbers in the right position
            final_list.insert(num, final_list[num + 1] * num_char)
            final_list.pop(num + 1)

    final_list = "".join(final_list)  # Finally we will join a list into a string again and print it out
    return final_list

print(decompress("(58,X),(666,c),(455,b),(58,B),(666,R),(455,5)"))

