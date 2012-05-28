def union(listA, listB) : 
	for i in listB : 
		if i not in listA : 
			listA.append(i)

def get_non_intersecting(listA, listB) :
	result = []
	for l in listA : 
		if l not in listB : 
			result.append(l)

	return result

def printList(list) : 
	for l in list : 
		print l