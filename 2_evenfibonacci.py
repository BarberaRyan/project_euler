import sys

def evenfib(a):
	sum = 0
	i = 1
	j = 2
	while a > j:
		if j % 2 == 0:
			sum += j
		tmp = j
		j += i
		i = j - i
	return sum

if __name__ == "__main__":
	a = int(sys.argv[1])
	b = evenfib(a)
	print("The sum is: " + str(b))
