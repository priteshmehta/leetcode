def canJump(self, nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	n = len(nums)
	last_element_index = n - 1
	i = 0
	if len(nums) <= 1:
		return True

	def jump(index, jump):
		new_index = index+jump # 2
		while(jump != 0):
			if new_index >= n: # true
				# new max jump value would within range
				jump(index, new_index - last_element_index)
			else:
				new_element = nums[new_index] + jump
				if (new_index+new_element) >= last_element_index:
					return True
				else:
					jump(new_index, new_element)
		return False

	while(i < n):
		if nums[i] == 0:
			return False
		if jump(i, nums[i]):
			return True
		i += 1

	return False

