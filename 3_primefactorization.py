import sys
import math

def primeTest(a):
	if a % 2 == 0 & a != 2:
		return False
	if a == 3:
		return True
	for i in range(3, math.floor(math.sqrt(a)), 2):
		if a % i == 0:
			return False
	return True

def primeFact(a):
	if primeTest(a):
		return a

	if a%2 == 0:
		while (a % 2 == 0):
			a = a/2
	if a == 1:
		return 2
	i = 3
	while (a > i):
		if primeTest(i):
			if a%i == 0:
				if a/i == 1:
					return i
				else:
					a = a/i
		i+= 2

	return a




if __name__ == "__main__":
	a = int(sys.argv[1])
	b = primeFact(a)
	print("The largest prime factor is: " + str(b))
