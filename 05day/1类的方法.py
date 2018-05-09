class Dog():
	comt =2
	def __init__(self,name):
		self.name =name
		comt = 1
	def wark(self):
		print("嗷嗷叫")
	@classmethod
	def lac(cls):
		print("执行")
	


taidi = Dog("泰迪")
taidi.lac()
taidi.wark()
print(Dog.comt)
print(taidi.lac())
