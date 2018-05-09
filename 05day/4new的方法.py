class Dog():
	__int = None
	__init_ll = False		

	def __init__(self,name):
		if Dog.__init_ll == False:
			self.name = name
			Dog.__init_ll = True


	def __new__(cls,name):
		if cls.__int == None:
			cls.__int = object.__new__(cls)
			return cls.__int
		else:
			return cls.__int


god = Dog("huahua")
god1 = Dog("haha")
god2 = Dog("wuwu")



print(id(god))
print(id(god1))
print(id(god2))

print(god.name)
print(god1.name)
print(god2.name)
