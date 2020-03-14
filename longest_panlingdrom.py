def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    str_len = len(s)
    uniq_char_len = len(set(s))
    longest_paling_str = ""
    if str_len < 2:
        return s
    elif str_len == uniq_char_len:
        return ""
    else:
        for i in range(str_len-1):
            #tmp_set = set(s[i])
            sub_str = s[i]
            for j in range(i+1, str_len):
                sub_str += s[j] 
                rev_str  = sub_str[::-1]
                str1 = "".join(s[i:j+1])
                str2 = rev_str
                if str1 == str2:
                    if len(longest_paling_str) < len(str2):
                        longest_paling_str = str1
                        print ("longest_paling_str: ", longest_paling_str)
    return longest_paling_str

#ans = longestPalindrome("jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx")
#print(ans)

import functools

#@functools.lru_cache(maxsize=128)

def longestPalindrome1(s):
    str_len = len(s)
    if str_len == 0:
        return
    else:
        sub_str = s[0]
        for i in range(1, str_len):
            sub_str += s[i] 
            rev_str  = sub_str[::-1]
            #print(sub_str, rev_str)
            if rev_str == sub_str:
                pass
                #print(sub_str)
                #if len(sub_str) > longest_paling_str:                
                #    longest_paling_str = len(sub_str)
                #    print(longest_paling_str)
        return longestPalindrome(s[1:])
        
        '''
        sub_str = s[i]
        for j in range(i+1, str_len):
            sub_str += s[j] 
            rev_str  = sub_str[::-1]
            str1 = "".join(s[i:j+1])
            str2 = rev_str
            if str1 == str2:
                if len(longest_paling_str) < len(str2):
                    longest_paling_str = str1
                    print ("longest_paling_str: ", longest_paling_str)
    return longest_paling_str
    '''

import timeit
longest_paling_str = 1
a = timeit.timeit('longestPalindrome1("ababa")', globals=globals(), number=1)
print(a)

#print(ans)


