

def maxCrossingSum(arr, l, m, h):       
    # Include elements on left of mid. 
    sm = 0
    left_sum = -1000000000
      
    for i in range(m, l-1, -1): 
        sm = sm + arr[i] 
        if (sm > left_sum): 
            left_sum = sm 

    # Include elements on right of mid 
    sm = 0
    right_sum = -1000000000
    for i in range(m + 1, h + 1): 
        sm = sm + arr[i] 
        if (sm > right_sum): 
            right_sum = sm 
    return left_sum + right_sum; 

def maxSubArray(nums,l, h):
    if (l == h): 
        return nums[l] 

    m = (l + h) // 2

    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the  
    #     subarray crosses the midpoint  
    return max(maxSubArray(nums, l, m),  maxSubArray(nums, m+1, h),  maxCrossingSum(nums, l, m, h)) 

a = [-2, -5, 6, -2, -3, 1, 5, -6]
max_sum = maxSubArray(a, 0, len(a)-1)
#max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 