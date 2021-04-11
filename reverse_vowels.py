# Reverse the vowels
# input: "hello"
# output: "holle"

def reverseVowels(s):
  i = 0
  n = len(s)
  new_str = []
  vowels = {'a', 'e', 'i', 'o', 'u'}
  v = []
  while i < n:
    if s[i].lower() in vowels:
        v.append(s[i])
    new_str.append(s[i])
    i += 1

  #replace blankspace with vowels in reverse
  for index, c in enumerate(new_str):
    if len(v) == 0:
      break
    if c.lower() in vowels:
      new_str[index] = v.pop()
  return ''.join(new_str)

print(reverseVowels("leetcode"))