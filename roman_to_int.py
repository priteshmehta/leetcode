def roman_to_int(roman_num):
    roman_symbols = { "I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000 }
    roman_symbols2 = { "IV": 4, "IX":9, "XL": 40, "XC":90, "CD": 400, "CM": 900 }
    i = 0
    result = 0
    while i < len(roman_num):
        if i+1 < len(roman_num):
            n = roman_symbols2.get((roman_num[i] + roman_num[i+1]), None)
            if n: 
                result += n
                i+=2
                continue
        n = roman_symbols.get(roman_num[i], None)
        if n:
            result += n
        else:
            print("invalid roman number")
            return 0
        i+=1

    return result

print("roman to integer coverter")
print(roman_to_int("XCVIII"))
print(roman_to_int("XVI"))
