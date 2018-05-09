class Dog():
	_int = None
	_intt = False
	def __new__(cls,name):
		if cls._int == None:
			cls._int = object.__new__(cls)
			return cls._int
		else:
			return cls._int


	def __init__(self,name):
		if Dog._intt == False:
			self.name = name
			Dog._intt = True








dog = Dog("haha")
dog1 = Dog("lala")
dog2 = Dog("wuwu")

print(dog.name)
print(dog1.name)
print(dog2.name)

print(id(dog))
print(id(dog1))
print(id(dog2))
