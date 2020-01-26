
class Person:
	pass #An empty block
	

p = Person()
print(p)

class Person:
	"""docstring for Person"""
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age 
		self.gender = gender

	def say_hi(self):
		print('Hello, my name is ', self.name)	
	def say_age(self):
		print('Hello, my age is ', self.age)
	def say_gender(self):
		print('Hey,i am ', self.gender)

p = Person('Htet Yal Kyaw', 21, "Male")
p.say_hi()
p.say_age()
p.say_gender()

		