class Dog():
	def __init__(self):
		self.__age = 1

	def call(self):
		print("汪汪叫")

	def setAge(self,age):
		if age <= 0:
			print("输入错误")
		else:
			self.__age = age

	def getAge(self):
		return self.__age

	def __str__(self):
		return "狗的年龄是%s"%self.__age



taidi = Dog()
taidi.setAge(5)
print(taidi.getAge())
print(taidi)
taidi.call()
