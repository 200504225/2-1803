class OP():
	def __init__(self,nau,nau1):
		self.nau = nau
		self.nau1 = nau1

	def geet(self):
		pass


class Jia(OP):
	def geet(self):
		return self.nau+self.nau1

class Jian(OP):
	def geeet(self):
		return self.nau+self.nau1

class Cheng(OP):
	def geet(self):
		return self.nau*self.nau1

class Chu(OP):
	def geet(self):
		if self.nau1 !=0:
			return self.nau/self.nau1
		else:
			print("输入错误")

j = Cheng(64,58)
print(j.geet())
