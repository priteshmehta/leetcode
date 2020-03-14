#https://leetcode.com/problems/multiply-strings/
def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_str = "0123456789"
        stoi_dict = {c:i for (i,c) in enumerate(num_str)}
        itos_dict = {i:c for (i,c) in enumerate(num_str)}
        def convert_int(num):
            num_length = len(num)
            n = 0
            for char in num:
                n = n + stoi_dict[char] * 10**(num_length - 1)
                num_length -= 1
            return n
        def convert_str(num):
            num_str = ""
            if num < 9:
                return itos_dict[num]
            while num > 9:
                digit = num % 10
                num = num//10
                num_str = itos_dict[digit] + num_str
            
            num_str = itos_dict[num] + num_str
            return num_str
        
        n1 = convert_int(num1)
        n2 = convert_int(num2)
        return convert_str(10)         
        

                 
ans = multiply("12312312312312321231231231231232123123123123123212312312312312329798797997979797998799897997979797", "12312312312312321231231231231232123123123123123212312312312312329798797997979797998799897997979797")           
print(ans)

        
