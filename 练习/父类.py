class Father():

	def makemoney(self):
		print("双手赚钱")

	def __init__(self,name):
		self.name =name
	def __str__(self):
		return self.name
class Son(Father):
	
	def makemoney(self):
		print("用脑子")
		Father().makemoney(self)
	def __init__(self,name):
		Father.__init__(self,name)
xiaoming=Son("小明")

print(xiaoming)	
