def even_odd(numlist, oddoreven):
	oddlist = []
	evenlist = []
	if oddoreven == "odd":
		for element in numlist:
			if element % 2 != 0:
				oddlist.append(element)
		return oddlist
	elif oddoreven == "even":
		for element in numlist:
			if element % 2 == 0:
				evenlist.append(element)
		return evenlist

print(even_odd([6 ,7 ,3 ,4 ,5 ,6 ,7 ,8], "odd"))





def addition(num_list):
    totalsum = 0
    for num in range(len(num_list)):
        totalsum += num_list[num]
    return totalsum

print(addition([6,7,3,4,5,6,7,8]))






def difference(num_list):
	totalsum = 0
	for element in num_list:
		totalsum += element
	return totalsum

print(difference([6,7,3,4,5,6,7,8]))






def multiplication(numlist):

	counter = len(numlist)
	result = 1
	while counter >= 1:
		result = result * numlist[0]
		numlist.pop(0)
		counter -= 1
	return result

print(multiplication([1,2,3,4,5,6,7,8,9]))






def division(numlist):
	pass

print(division([1,2,3,4,5,6,7,8,9]))