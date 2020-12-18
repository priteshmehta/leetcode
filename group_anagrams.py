def groupAnagrams(strs):
    def grp_annagram(sub_str):
            anagram_word1 = {}
            for s in sub_str:
                key = "".join(sorted(s))
                try:
                    anagram_word1[key].append(s)
                except KeyError:
                    anagram_word1[key] = [s]
            return anagram_word1.values()

    n = len(strs)
    if n == 0:
        return [[]]
    elif n == 1:
        return [strs]
    else: 
        word_dict = {}
        for s in strs:
            try:
                word_dict[len(s)].append(s)
            except KeyError:
                word_dict[len(s)] = [s]
        anagram_word = []
        for key in word_dict.keys():
            tmp_list = grp_annagram(word_dict[key])
            anagram_word.extend(tmp_list)
            

    print(anagram_word)
    return anagram_word
    



groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])