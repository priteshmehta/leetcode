def intToRomannum( num: int) -> str:
    roman_chars = {1: "I", 2:"II", 3:"III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
            50: "L", 40: "XL", 90: "XC" , 100: "C", 500: "D", 1000: "M", 400: "CD", 900: "CM"}
    roman_str = []
    i = 0
    if num in roman_chars.keys():
        return roman_chars[num]
    else:
        tmp1 = []
        while num > 10:
            digit = num % 10
            num = num // 10
            tmp1.append((10**i,digit))
            i += 1
    tmp1.append((10**i,num))
    print(tmp1)
    for n in tmp1[::-1]:
        #print(n[0], n[1])
        prod = n[0] * n[1]
        while prod > 0:
            if prod in roman_chars.keys():
                roman_str.append(roman_chars[prod])
                break
            else:
                if prod > 1000:
                    roman_str.append(roman_chars[1000])
                    prod -= 1000
                elif prod > 500:
                    roman_str.append(roman_chars[500])
                    prod -= 500
                elif prod > 100:
                    roman_str.append(roman_chars[100])
                    prod -= 100
                elif prod > 50:
                    roman_str.append(roman_chars[50])
                    prod -= 50
                else:
                    roman_str.append(roman_chars[10])
                    prod -= 10                            
    roman_str = ''.join(roman_str)
    return roman_str
            

#CVIII
print(intToRomannum(200))
#print(intToRomannum(1894))
#MCMXCIV