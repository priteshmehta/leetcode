# Plaingdrome number

def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""
	x_str = str(x)
	n = len(x_str)
	if n <= 1:
		return True
	start = 0
	end = n - 1
	while(start < end):
		if x_str[start] != x_str[end]:
			return False
		start += 1
		end -= 1
	return True


#print(isPalindrome(101))
#print(isPalindrome(-101))
print(isPalindrome(1000021))




