# https://leetcode.com/problems/most-common-word/

def mostCommonWord(paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        import collections
        import operator
        def santise(w):
            w = re.sub('[$,.:;?!]', '', w)
            return w.lower().strip("'").strip("\"")

        #words = paragraph.split(" ")
        words = re.split('[$.,\s+]', paragraph)
        print(words)
        banned_words = set([w.lower() for w in banned])
        word_count = {} 
        for word in words:
            word = santise(word)
            if word not in banned_words:
                if word != "":
                    try:
                        word_count[word] = word_count[word] + 1
                    except KeyError:    
                        word_count[word] = 1
        
        word_occurance = sorted(word_count.items(), key=operator.itemgetter(1))
        sorted_dict = collections.OrderedDict(word_occurance)
        used_word = word_occurance[-1]
        return used_word[0]
        


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
a = mostCommonWord(paragraph, banned)
print(a)