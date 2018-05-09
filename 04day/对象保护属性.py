class Dod():
	def __init__(self,name):
		self.__age = 1
		self.name = name
	
	def call(self):
		print("汪汪叫")

	def gerAge(self):
		return self.__age

	def __str__(self):
		return "狗的年龄是%s"%(selr.__age)

hashiqi= Dod("哈士奇")

