#quick sort
# Best and average case (O) long n - Complexity
# Worst case : (O) n2 - Complexity
# default sorting alog in many programming lang.

def quick_sort(a):
	if len(a) == 0:
		return []
	pivot_index = len(a) // 2
	pivot = a[pivot_index]
	left = []
	right = []
	for i, e in enumerate(a):
		if i != pivot_index:
			if e > pivot:
				right.append(e)
			else:
				left.append(e)

	return quick_sort(left) + [pivot] + quick_sort(right)


a = [5,2,1,4,5]
b = quick_sort(a)
print(b)


