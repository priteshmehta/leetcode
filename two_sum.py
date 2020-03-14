
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    input_dict = {}
    ele1 = ele2 = 0
    if len(nums) <2:
        print("Invalid list") 
        return []
    if len(nums) == 2: 
        return [0, 1]

    for index, item in enumerate(nums):
        try:
            input_dict[item].append(index)
        except:
            input_dict[item] =  [index]            
    #print(input_dict)
    for i in range(len(nums)):
        try:
            val1 = nums[i] 
            val2 = target - val1 
            if val2 == val1 and len(input_dict[val2]) > 1:
                ele1, ele2  = i, input_dict[val2][1]
                break
            elif val2 != val1:
                print ("for ", i, val1, val2) 
                ele1, ele2  = i, input_dict[val2][0]
                break
        except KeyError:
            pass

    rtype = [ele1, ele2]
    return rtype

#print(twoSum([3,2,11,7], 9))
#print(twoSum([3,3,2,5], 6))
#print(twoSum([3,3], 6))
print(twoSum([3,2,4], 6)) #1,2


