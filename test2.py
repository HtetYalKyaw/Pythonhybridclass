# def do_global():
# 	global spam
# 	spam = "global spam"

# spam = "test spam"
# do_global()
# print("After global assigment:", spam)


def func():
	nonlocal x
	print('x is', x)

	x = 5
	print("Value of x is :", x)

x = 10
func()
print("After nonlocal assigment:", spam)



def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	spam = "test spam"
	# do_local()
	# print("After local assigment:", spam)
	do_nonlocal()
	print("After nonlocal assigment:", spam)

scope_test()