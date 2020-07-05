#Format: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
#Example: python letters.py e r p r e n m u i
import sys

input = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]]

finarr = []
dictionary = open("dictionary.txt", "r")
for x in dictionary:
	finalArray = []
	inputarray = []

	returnvalue = x.strip("\n")
	for n in input:
		inputarray.append(n)
	word = list(x.strip("\n"))

	for x in range(0, 9):
		for y in word:
			if y in inputarray:
				finalArray.append(y)
				inputarray.remove(y)
				word.remove(y)

	if len(word) == 0:
		finarr.append(returnvalue)
finret = ''
secondfinret = ''
thirdfinret = ''
maxcount = 0
for x in finarr:
	if len(x) >= maxcount:
		thirdfinret = secondfinret
		secondfinret = finret
		finret = x
		maxcount = len(x)

print(finret)
print(secondfinret)
print(thirdfinret)
	
