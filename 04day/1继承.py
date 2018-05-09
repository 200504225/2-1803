class Dog():
	def __init__(self):
		self.__name = "泰迪"

	def name(self):
		return self.__name

	def call(self):
		print("汪汪叫")

	def eat(self):
		print("吃狗粮")

	def __bite(self):
		print("咬人")

	def sbite(self):
		self.__bite()


class Taidi(Dog):
	pass



taidi = Taidi()
taidi.call()
taidi.eat()
taidi.sbite()
print(taidi.name())
