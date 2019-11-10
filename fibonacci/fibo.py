 def fib(n):	# write Fibonacci series up to n
 	"""Print a Fibonacci series up to n."""
 	a , b = 0, 1
 	while a < n:
 		print(a,end='')
 		a, b = b, a+b
 	print()
	
def fib2(n): # retrun Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n"""
	result = [ ]
	a, b = 0, 1 
	while a < n:
		result.append(a)	#see below
		a , b = b , a+b
	return result
# fib(100)
# fib2(100)


 # a = 0
 # b = 1

 # while  a < n:
 # 	print(a)
 # 	a = b 
	# b = a+b


