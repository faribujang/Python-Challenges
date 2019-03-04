def mean(n):
	if len(n) == 0:
		print("List length must be greater than 0")
		# break

	a = sum(n)
	b = a/len(n)

	return b

f = [1, 2, 3, 4, 5]

print(mean(f))