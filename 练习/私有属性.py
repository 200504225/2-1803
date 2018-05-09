class Dog():
	def __init__(self):
		self.__age = 1

	def wark(self):
		print("汪汪叫")
	def setAge(self,age):
		if age <= 0:
			print("输入有误")
		else:
			self.__age = age
	
	def __str__(self):
		return "狗的年龄是%s"%self.age




taidi = Dog(10)
print(taidi)
taidi.wark
