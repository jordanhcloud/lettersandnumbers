#Format: Target, 1st, 2nd, 3rd, 4th, 5th, 6th
#Example: python numbers.py 336 75 50 7 6 5 2
import sys; import itertools; result = 0; count = 0; numbers = [int(sys.argv[x + 2]) for x in range(6)]; target = int(sys.argv[1]); 
	

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y
 
def getoperator(operatorvalue, firstvalue, secondvalue):
	result = 0
	if operatorvalue == 0:
		result = add(firstvalue, secondvalue)
	if operatorvalue == 1:
		result = subtract(firstvalue, secondvalue)
	if operatorvalue == 2:
		result = multiply(firstvalue, secondvalue)
	if operatorvalue == 3:
		result = divide(firstvalue, secondvalue)
	return result
	
def getoperatorfromvalue(operatorvalue):
	result = ''
	if operatorvalue == 0:
		result = "+"
	if operatorvalue == 1:
		result = "-"
	if operatorvalue == 2:
		result = "*"
	if operatorvalue == 3:
		result = "/"
	return result
	
def getprocess(array, x, x1, x2, x3, x4):
	output = str(array[0]) + getoperatorfromvalue(x) + str(array[1]) + getoperatorfromvalue(x1) + str(array[2]) + getoperatorfromvalue(x2) + str(array[3]) + getoperatorfromvalue(x3) + str(array[4]) + getoperatorfromvalue(x4) + str(array[5])
	return output

def getprocess2(array, x, x1, x2, x3):
	output = str(array[0]) + getoperatorfromvalue(x) + str(array[1]) + getoperatorfromvalue(x1) + str(array[2]) + getoperatorfromvalue(x2) + str(array[3]) + getoperatorfromvalue(x3) + str(array[4])
	return output

def getprocess3(array, x, x1, x2):
	output = str(array[0]) + getoperatorfromvalue(x) + str(array[1]) + getoperatorfromvalue(x1) + str(array[2]) + getoperatorfromvalue(x2) + str(array[3])
	return output

def getprocess4(array, x, x1):
	output = str(array[0]) + getoperatorfromvalue(x) + str(array[1]) + getoperatorfromvalue(x1) + str(array[2])
	return output
	
def getprocess5(array, x):
	output = str(array[0]) + getoperatorfromvalue(x) + str(array[1])
	return output

finalArray = []
myit = iter(numbers)
for val in range(0, len(numbers) - 1):
	for x in range(0, 4):
		for x1 in range(0, 4):
			for x2 in range(0, 4):
				for x3 in range(0, 4):
					for x4 in range(0, 4):
						answer = getoperator(x4, getoperator(x3, getoperator(x2, getoperator(x1, getoperator(x, numbers[0], numbers[1]), numbers[2]), numbers[3]), numbers[4]), numbers[5])
						if(answer == int(sys.argv[1])):
							finalArray.append(getprocess(numbers, x, x1, x2, x3, x4))
	numbers.append(numbers[0])
	numbers.pop(0)
	
myit = iter(numbers)
for subset in itertools.permutations(myit, 5):
	for x in range(0, 4):
		for x1 in range(0, 4):
			for x2 in range(0, 4):
				for x3 in range(0, 4):
					answer = getoperator(x3, getoperator(x2, getoperator(x1, getoperator(x, subset[0], subset[1]), subset[2]), subset[3]), subset[4])
					if(answer == int(sys.argv[1])):
						finalArray.append(getprocess2(subset, x, x1, x2, x3))

myit = iter(numbers)
for subset in itertools.permutations(myit, 4):
	for x in range(0, 4):
		for x1 in range(0, 4):
			for x2 in range(0, 4):
				answer = getoperator(x2, getoperator(x1, getoperator(x, subset[0], subset[1]), subset[2]), subset[3])
				if(answer == int(sys.argv[1])):
					finalArray.append(getprocess3(subset, x, x1, x2))
	
myit = iter(numbers)
for subset in itertools.permutations(myit, 3):
	for x in range(0, 4):
		for x1 in range(0, 4):
			answer = getoperator(x1, getoperator(x, subset[0], subset[1]), subset[2])
			if(answer == int(sys.argv[1])):
				finalArray.append(getprocess4(subset, x, x1))

myit = iter(numbers)
for subset in itertools.permutations(myit, 2):
	for x in range(0, 4):
			answer = getoperator(x, subset[0], subset[1])
			if(answer == int(sys.argv[1])):
				finalArray.append(getprocess5(subset, x))

x = set(finalArray)
try:
	print(next(iter(x)))
except:
	print("No possible solutions")
