import sys
import math

def sieveSol(a):
	#Create Sieve first
	x = [1 for i in range(a)]
	for i in range(2, math.floor(math.sqrt(a)) + 1, 1):
		for j in range(i + i, a, i):
			x[j] = 0
		i += 1
	#Test Sieve values
	for i in range(math.floor(a/2), 0, -1):
		if x[i] == 1:
			if (a % i == 0):
				return i


if __name__ == "__main__":
	a = int(sys.argv[1])
	b = sieveSol(a)
	print("The largest prime factor is: " + str(b))
