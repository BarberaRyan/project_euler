import sys

def multiples(a, x, y):
	sum = 0;
	for i in range(a):
		if (i%x == 0 or i%y == 0):
			print("Adding: " + str(i))
			sum += i
	return sum


if __name__ == "__main__":
	a = int(sys.argv[1])
	b = multiples(a, 3, 5)
	print("The sum is: " + str(b))
