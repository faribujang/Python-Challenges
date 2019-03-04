def sum():
	x = 2
	n = 100

	count = 0
	total = 2

	while count != (n-2)/2:
		x = x+2
		total += x
		count += 1

	return total

print(sum())