#A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    def get_sum_of_squares(num):
        num_str = str(num)
        result = sum([int(n)**2 for n in num_str])
        return result
    already_visited = [1,n]
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n%10 == 0:
            return True
    else:
        new_num = get_sum_of_squares(n)
        while new_num not in already_visited:
            print(new_num)
            already_visited.append(new_num)
            if new_num%10 == 0:
                return True
            new_num = get_sum_of_squares(new_num)
    
    return new_num == 1

ans = isHappy(19)
print(ans)