def stringShift(s, shift):
    """
    :type s: str
    :type shift: List[List[int]]
    :rtype: str
    """
    s1 = list(s)
    n  = len(s1)
    for (direction, amount) in shift:
        amount = amount % n 
        print(amount)
        if direction == 0:
            #means shift to left by 1. "abc" -> "bca"
            tmp = s1[amount:] + s1[:amount]
            s1 = tmp
            
        elif direction == 1:
            # a right shift by 1 means remove the last character of s and add it to the beginning.
            #means shift to right by 2. "bca" -> "cab"
            remaining = n - amount
            s1 = s1[remaining:] + s1[:remaining]

        print(s1)

    print(''.join(s1))

s = "abc"
shift = [[0,1],[1,2]]
stringShift(s,shift)
