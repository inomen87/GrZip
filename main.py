
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
compress_percent = (len(outputstring) / len(inputstring) * 100)

if (100 - compress_percent) > 0:
	print(outputstring)
	print("Compression successful. Space saved: " + str(round(100 - compress_percent)) + "%")
else:
	print("Compression unsuccessful. Input too short.")
