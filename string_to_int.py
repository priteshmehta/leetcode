#https://leetcode.com/problems/string-to-integer-atoi/
import re
def myAtoi(s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        pattern = '(^[-+]?\d+).*$'
        valid_nums = set({'0','1', '2', '3', '4', '5', '6', '7' ,'8', '9', '+', '-'})
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        length = len(s)
        nums = []
        if length == 0:
            return 0
        elif s[0] not in valid_nums:
            return 0
        else:
            result = re.match(pattern, s)
            if result:
                #print(result.group(1))
                nums = result.group(1)
            else:
                return 0 
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and nums[0] in ["+", "-"]:
            return 0
        else:
            int_num = int(nums)
            if int_num < INT_MIN:
                result = INT_MIN
            elif int_num > INT_MAX:
                result = INT_MAX
            else:
                result = int_num
            return result
    
ans = myAtoi("+-")
print(ans)


