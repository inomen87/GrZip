def compress(inputstring, delimiter):
    """ Function compresses an alphanumeric input string(e.g. "zzzzaaaa") and returns
     a string in this format: "{4,z},{4,a}".
     "{" and "}" are delimiters and can be changed in the function arguments.  """
    if len(delimiter) != 2 or len(inputstring) < 1:
        return None

    outputstring = ""
    counter = 1

    for num in range(1, len(inputstring)):
        if inputstring[num] == inputstring[num - 1]:
            counter += 1
        else:
            outputstring += delimiter[0] + str(counter) + "," + inputstring[num - 1] + delimiter[1] + ","
            counter = 1

    outputstring += delimiter[0] + str(counter) + "," + inputstring[-1] + delimiter[1]
    compress_percent = (len(outputstring) / len(inputstring) * 100)

    if (100 - compress_percent) > 0:
        return outputstring, "Compression successful. Space saved: " + str(round(100 - compress_percent)) + "%"
    else:
        return outputstring, "Compression unsuccessful. Input too short."





print(compress("zzzzaaaa", delimiter=["{","}"]))


