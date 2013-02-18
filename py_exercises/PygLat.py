# PygLat.py - Pig Latin Translator
# Date: 01-19-2013

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	if first == ('a' or 'e' or 'i' or 'o' or 'u'):
		new_word = word + pyg
		print new_word
	else:
		new_word = word[1:] + first + pyg
		print new_word
else:
	print 'Empty or not an alphabetic string!'
