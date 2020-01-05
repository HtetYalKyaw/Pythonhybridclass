# def scope_test():
# 	def do_local():
# 		spam = "local spam"

# 	def do_nonlocal():
# 		nonlocal spam
# 		spam = "nonlocal spam"

# 	def do_global():
# 		global spam
# 		spam = "global spam"


# 	spam = "test spam"
# 	do_local()
# 	print("After local assigment:", spam)
# 	do_nonlocal()
# 	print("After nonlocal assigment:", spam)
# 	do_global()
# 	print("After global assigment:", spam)


# scope_test()
# print("In global scope:", spam)



# def say_hello():
# 	print('Hello World')
# say_hello()


# function parameter
# a = input('Please entr A value: ')
# b = input('Please entr B value: ')

# def print_max(a, b):
# 	if a > b:
# 		print(a, 'is maximun')
# 	elif a == b: 
# 		print(a, 'is equal to', b)
# 	else:
# 		print(b, 'is maximun')

# print_max(a,b)

# print_max(3,4)
# print_max(5,4)
# print_max(7,7)


# Local Variables

# def func(x):
# 	print('x is', x)
# 	x = 2 
# 	print('Changed local x to', x)

# x = 10
# func(x)
# print('x is still', x)

# ---------------------------------------------------------------------------

# def func(y):
# 	print('y is', y)
# 	y = 10 
# 	print('Changed local y to', y)

# def funx(y):
# 	print('y is', y)
# 	y = x + y
# 	print('Y is changed x + y', y)

# x = 40
# y = 20
# func(y)
# funx(y)
# print('y is still', y)

# -----------------------------------------------------------
# global Variables


# def func():
# 	global x 

# 	print('x is', x)
# 	x = 12 
# 	print('Changed global x to', x)

# x = 5	
# func()
# print('Value of x is ',x)

# -----------------------------------------------------------

# eg
# def func():
# 	global y 
# 	print('y is ',y )

# 	y = 100
# 	print('Value of y is:' ,y)

# y = 50
# func()

# print('Value of y: ',y)


# print(20 > 20)
# print(20 == 20)
# print(20 < 10)
# print(bool("Hello World"))
# print(bool(20))


# # Python Conditions 

# Equals					-> x == y
# Not Equals				-> x != y
# Less than				-> x <  y
# Less than or equal to	-> x <= y
# greater than			-> x >  y
# greater than or equal to-> x >= y

# -----------------------------------------------------------
# def do_global():
# 	global spam
# 	spam = "global spam"

# spam = "test spam"
# do_global()
# print("After global assigment:", spam)

def do_nonlocal():
	
	nonlocal spam
	spam = "nonlocal spam"

	spam = "test spam"
do_nonlocal()
print("After nonlocal assigment:", spam)


# def func():
# 	nonlocal x
# 	print('x is', x)

# 	x = 5
# 	print("Value of x is :", x)

# x = 10
# func()
# print("After nonlocal assigment:", spam)



# def scope_test():
# 	def do_local():
# 		spam = "local spam"

# 	def do_nonlocal():
# 		nonlocal spam
# 		spam = "nonlocal spam"

# 	spam = "test spam"
# 	# do_local()
# 	# print("After local assigment:", spam)
# 	do_nonlocal()
# 	print("After nonlocal assigment:", spam)

# scope_test()