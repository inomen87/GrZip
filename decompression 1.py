counter = 1


def decompress(inputstring):
    global counter

    numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    inputlist = list(inputstring)

    for num in range(len(inputlist)):
        if counter == 1:
            # Here we check to see if current character is a number or a letter. We only need numbers.
            if inputlist[num] in numlist:  # .isdigit()
                # The if statement below checks if we have a case of two digit number
                # before a character in the input string.
                if inputlist[num + 1] not in numlist:  # alphabetical character
                    if inputlist[num] == "1":
                        inputlist.pop(num)
                        decompress(inputlist)
                    else:
                        one_number = int(inputlist[num])
                        # We subtract 1 from total number because we already have 1 letter in the input string.
                        one_number_correct = one_number - 1
                        # Here we insert characters instead of numbers, same as number before the letter -1.
                        inputlist.insert(num, inputlist[num + 1] * one_number_correct)
                        # Here we delete the number.
                        inputlist.pop(num + 1)
                        decompress(inputlist)
                else:  # second number
                    two_numbers = int(inputlist[num] + inputlist[num + 1])
                    two_numbers_correct = two_numbers - 1
                    inputlist.insert(num, inputlist[num + 2] * two_numbers_correct)
                    inputlist.pop(num + 1)
                    inputlist.pop(num + 1)
                    decompress(inputlist)

    if counter == 1:
        inputlist = "".join(inputlist)
        print(inputlist)
        print(len(inputlist))
        counter += 1


decompress("11a1a33f")
