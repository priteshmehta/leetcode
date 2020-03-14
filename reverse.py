
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    MAX_SIGNED_INT_VALUE = 2**31 - 1 
    if x > MAX_SIGNED_INT_VALUE:
        return 0
    num = abs(x)
    str_num = str(num)
    rev = list(str_num)[::-1]
    t = "".join(rev)
    rtype = int(t)
    if rtype > MAX_SIGNED_INT_VALUE:
        return 0
    if x < 0:
        rtype = 0 - rtype
    return rtype

ans = reverse(1534236469)
print(ans)
