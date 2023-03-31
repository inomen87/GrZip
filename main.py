
inputstring = "z"
outputstring = ""
counter = 1

for num in range(1, len(inputstring)):
	if inputstring[num] == inputstring[num - 1]:
		counter += 1
	else:
		outputstring += "(" + str(counter) + "," + inputstring[num - 1] + ")" + ","
		counter = 1


outputstring += "(" + str(counter) + "," + inputstring[-1] + ")"
pinta = (len(outputstring) / len(inputstring)  * 100)

if (100 - pinta) > 0:
	print(outputstring)
	print("Compression successful. Space saved: " + str(round(100 - pinta)) + "%")
else:
	print("Compression unsuccessful. Input too short.")






