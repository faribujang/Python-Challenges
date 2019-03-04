def median(n):

	n.sort()
	x = len(n)

	if x%2 != 0:
		return n[int((x-1)/2)]

	else:
		return (n[int((x-1)/2)] + n[int(x/2)])/2

f = [5, 10, 20, 40, 80, 160, 320, 640]

print(median(f))