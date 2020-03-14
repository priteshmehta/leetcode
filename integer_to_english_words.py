#https://leetcode.com/problems/integer-to-english-words/
def numberToWords(num: int) -> str:
    num_to_word = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4":"Four", "5": "Five",
                "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine", "10": "Ten",
                "11": "Eleven", "12": "Twelve", "13": "Thirteen", 
                "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen",
                "18": "Eighteen", "19": "Nineteen", "20": "Twenty", "30": "Thirty", 
                "40": "Forty", "50": "Fifty", "60": "Sixty", "70": "Seventy",
                "80": "Eighty", "90": "Ninety"}
    prefix  = {1:"", 2:"Thousand", 3: "Million", 4: "Billion"}
    
    num_str = str(num)
    length = len(num_str)
    words = ""
    if length == 0 or length > 10:
        return "Number not supported"

    if num_str in num_to_word.keys():
        return num_to_word[num_str]
    
    def get_words(nums, pos):
        words = ""
        i = 1
        for n in nums:
            if n != '0':
                if i == 1:
                    words = num_to_word[n]
                if i == 2:
                    tmp = n + prev_num
                    if tmp in num_to_word.keys():
                        words = num_to_word[tmp]
                    else:
                        n = int(n)*10                    
                        words = num_to_word[str(n)] + " " + words
                if i == 3:
                    words = num_to_word[n] + " Hundred " + words
            i += 1
            prev_num = n  
        if pos != 1:
            if words != "":      
                words = words + " " + prefix[pos] + " "
        return words
           
    i = 0
    t = ""
    grp_count = 1
    ans = ""
    for num in num_str[::-1]:
        if i != 3:
            t = t + num 
        else:
            ans = get_words(t, grp_count) + ans
            grp_count += 1
            t = num
            i = 0
        i += 1

    ans = get_words(t, grp_count) + ans
    import re
    ans = re.sub(' +', ' ',ans)
    return ans.strip()

    

#print(numberToWords(1234567891)) 
print(numberToWords(1000))
#0000

#1 000 000


'''
numberToWords(0)
numberToWords(100)
numberToWords(111)
numberToWords(600)
numberToWords(9999)
numberToWords(90990)
numberToWords(100900)
numberToWords(8100911)
'''




#00900
#7890900
#49