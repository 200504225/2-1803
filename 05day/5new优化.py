class Dog():
	__int = None
	__int_ll = False
	def __new__(cls,name):
		if cls.__int == None:
			cls.__int = object.__new__(cls)
			return cls.__int
		else:
			return cls.__int

	def __init__(self,name):
		if Dog.__int_ll == False:
			self.name = name
			Dog.__int_ll = True



dog = Dog('huahua')
dog1 = Dog('heihei')
dog2 = Dog('wuwu')

print(dog.name)
print(dog1.name)
print(dog2.name)


print(id(dog))
print(id(dog1))
print(id(dog2))
