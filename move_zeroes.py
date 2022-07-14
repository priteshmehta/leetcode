#[0,1,0,3,12]
def moveZeroes(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            if i != j:
                nums[j] = nums[i]
            j+=1
    
    while j < n:
        nums[j] = 0
        j+=1
        
    print(nums)       
            

moveZeroes([0,1,0,0,0,0,3,12,0,0,0,0])
moveZeroes([0,0,0,0,0,0,0,12,0,0,0,0,1])
moveZeroes([1])
moveZeroes([0])
