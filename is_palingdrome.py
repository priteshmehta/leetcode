def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    t = []
    reverse_num = 0
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        last_digit = x%10 
        t.append(last_digit)
        new_num = int(x/10)
        while new_num >= 10: 
            last_digit = new_num%10 
            new_num = int(new_num/10)
            t.append(last_digit)
        t.append(new_num)
        total_zero =  len(t) - 1  
        for digits in t:
            reverse_num += digits*10**(total_zero)
            total_zero -= 1
            #print("reverse_num", reverse_num)
        print(reverse_num)
        return (reverse_num == x)


ans = isPalindrome(12221)
print(ans)