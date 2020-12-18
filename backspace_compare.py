def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    def backspace_str(S):
        j = 0
        S = list(S)
        for i, s in enumerate(S):
            if s == '#':
                if j > 0:
                    j -= 1
            else:
                #print(j)
                #print(S[i])
                S[j] = S[i]
                j += 1
        print(S[:j])
        return ''.join(S[:j])

    str1 = backspace_str(S)
    str2 = backspace_str(T)
    return str1 == str2


ans = backspaceCompare("ab##","c#d#")   
print(ans)

