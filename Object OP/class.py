Classes 

class Person:
	pass #An empty block
	

p = Person()
print(p)


# Methods

class Person:
	def say_hi(self):
		print('Hello, how are you ?')

p = Person()
p.say_hi()


# __init__method

class Person:
	def __init__(self, name):
		self.name = name 

	def say_hi(self):
		print('Hello, my name is ', self.name)

p = Person('Swarrop')
p.say_hi()		
---------------------


class  SchoolMember:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))

	def tell(self):

		print('Name: "{}" Age:"{}"'.format(self.name, self.age),end="")

class Teacher(SchoolMember):

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks 
		print('(Initialized Student:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))				

class Student(SchoolMember):

	def __init__(self, name, age , marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))
			
			