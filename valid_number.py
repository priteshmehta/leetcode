#https://leetcode.com/problems/valid-number/

def isNumber(s):
        """
        :type s: str
        :rtype: bool
        """
         """
        :type s: str
        :rtype: bool
        """
        import re
        s = s.strip()
        pattern = '^[0-9]+[.]?[0-9]*$'
        pattern_with_e = '^[0-9]+[e][-0-9]+$'
        pattern_with_e_dot1 = '^[0-9]+[.]?e[+-]?[0-9]+$'
        pattern_with_e_dot = '^[0-9]+[.]?[0-9]+e[+-]?[0-9]+$'
        
        valid_nums = set({'0','1', '2', '3', '4', '5', '6', '7' ,'8', '9', '+', '-', '.'})
        valid_digits = set({'0','1', '2', '3', '4', '5', '6', '7' ,'8', '9', '.'})
        if len(s) == 0:
            return False
        elif s[0] not in valid_nums:
            return False
        elif s[-1] not in valid_digits:
            return False
        elif s[0] in ['+', '-', '.'] and len(s) == 1:
            return False
        if s.count('.') > 1:
            return False
        elif s[0] in ['+', '-', "."]:
            t = s[0]
            s = s[1:]
            if t in ['+','-'] and s[0] == '.':
                s = s[1:]
        else:
            pass
        print(s)
        if re.match(pattern, s):
            return True
        elif re.match(pattern_with_e, s):
            return True
        elif re.match(pattern_with_e_dot, s):
            return True
        elif re.match(pattern_with_e_dot1, s):
            return True
        else:
            return False


#print(isNumber("asdaasd9"))
print(isNumber("0"))
#print(isNumber("0.1"))
#print(isNumber("1e1"))
#print(isNumber("e1"))

