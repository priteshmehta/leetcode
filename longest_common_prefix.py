#https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""

    unique_strs = list(set(strs))
    if len(unique_strs) == 1:
        return unique_strs[0]

    longest_str = unique_strs[0]
    longest_str_len = len(longest_str)
    for s in unique_strs[1:]:
        i = 0
        j = 0
        while j < len(s) and i < longest_str_len:
            print(i,j)
            if longest_str[i] != s[j]:
                break
            i+=1 
            j+=1

        if i == 0:
            longest_str = ""
            break
        else:
            longest_str = longest_str[:i] 
            longest_str_len = len(longest_str)
        print("New Longest String:", longest_str)
    return longest_str

ans = longestCommonPrefix(["flower","flow","flight"])
print(ans)