#Liner Search  = helps to find value from unsorted array O(n)
#binary Search  = to find value from sorted array


def binary_search(a, search_element):
	start = 0
	end = len(a) - 1

	while start <= end:
		middle = (start + end) // 2
		if search_element == a[middle]:
			return middle
		elif search_element > a[middle]:
			start = middle + 1
		else:
			end = middle - 1

	return -1


a = [1, 2, 3, 4, 5, 5]
index = binary_search(a, 3)
print(index)



