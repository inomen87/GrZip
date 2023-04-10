def even_odd(numlist, oddoreven):
	if isinstance(numlist, list):
		if isinstance(oddoreven, str):
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
		else:
			return None
	else:
		return None

print(even_odd([6 ,7 ,3 ,4 ,5 ,6 ,7 ,8], "odd"))




def addition(numlist):
	if isinstance(numlist, list):
		totalsum = 0
		for num in range(len(numlist)):
			totalsum += numlist[num]
		return totalsum
	else:
		return None

print(addition([6,7,3,4,5,6,7,8]))






def difference(numlist):
	if isinstance(numlist, list):
		totalsum = 0
		for element in numlist:
			totalsum += element
		return totalsum
	else:
		return None

print(difference([6,7,3,4,5,6,7,8]))






def multiplication(numlist):
	if isinstance(numlist, list):
		counter = len(numlist)
		result = 1
		while counter >= 1:
			result = result * numlist[0]
			numlist.pop(0)
			counter -= 1
		return result
	else:
		return None

print(multiplication([1,2,3,4,5,6,7,8,9]))






def division(numlist):
	pass

print(division([1,2,3,4,5,6,7,8,9]))