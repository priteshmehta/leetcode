#count sort
'''
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index
  stores the sum of previous counts.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7
'''

#create array to store count of each element
def count_sort(array):
	max_number = 100
	count_array = [0] * max_number

	#Count the occurance of each element
	for item in array:
		count_array[item] = count_array[item] + 1

	#sum occurance to all previous values
	prev_item = 0
	for index, item in enumerate(count_array):
		prev_item += item
		count_array[index] = prev_item

	#iterate the original array and place the element to the new index from count_array value
	output = [0]*(len(array)+1)
	for i, a in enumerate(array):
		#print("Item:",a)
		new_index = count_array[a]
		print(new_index)
		output[new_index] = a
		count_array[a] -= 1

	print(output)

count_sort([1, 4, 1, 2, 7, 5, 2])


