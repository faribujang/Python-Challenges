def squareroot():
	x = int(input("Enter number to square root: "))
	# if x <= 0 then Error

	a = 10

	# iterations = 0

	while(True):		#abs(f) not in range(-1,1)

		f = a*a - x

		f_prime = 2*a

		a = a - (f/f_prime)

		# iterations += 1

		if -0.1 < abs(f) < 0.1:	
			print(a)

			break

		# if iterations == 3:
		# 	print(a)

	# 	return a
	# print("Square root is:" + a)

#ALTERNATIVE METHOD

def squareroot_2(n):
	x = n
	y = 1
	a = 0.0001

	while((x-y) > a):
		x = (x+y)/2
		y = n/x

	return x

print(squareroot_2(4))