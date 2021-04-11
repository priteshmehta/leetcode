#Simple string compression

import unittest

def compress(s):
	output = []
	if len(s) == 0:
		return []

	output.append(s[0])
	i = 1
	counter = 0
	while i < len(s):
		if output[-1] == s[i]:
			counter += 1
		else:
			if counter > 0:
				output.append(str(counter))
				counter = 0
			else:
				output.append(s[i])

		i += 1
	return ''.join(output)

# using itetools

# from itertools import groupby
# import re
# def comporess2(string):
#    	return re.sub(r'(?<![0-9])[1](?![0-9])', '', ''.join('%s%s' % (char, sum(1 for _ in group)) for char, group in groupby(string)))


class compresssTest(unittest.TestCase):
	def setUp(self):
		print("test setup")

	def test_compress(self):
		self.assertEqual(compress("aaaaabbbcccd"), "a4b1c1")
		#self.assertTrue

	def test_compress(self):
		self.assertEqual(compress("abdb"), "abdb")


#to run python -m unittest <fileName>
if __name__ == '__main__':
	unittest.main()
	# print(compress("aaaaabbbcccd"))



