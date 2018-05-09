class Home():
	def __init__(self,add,area):
		self.add = add
		self.area = area
		self.accom = []
		self.dengs = []

	def __str__(self):
		msg = ("房子地址是%s\n房子的面积是%d平方米"%(self.add,self.area))
		return msg

	def addBed(self,bed):
		if self.area >= bed.getAred(): 
			self.accom.append(bed)
			self.area-= bed.getAred()
			print("已经放入房间")
			print(self.area)

		else:
			print("放入失败")
	def addlamp(self,lamp):
		self.dengs.append(lamp)

	def switch(self):
		if self.dengs[0].getIsopen():
			self.dengs[0].close()
		else:
			self.dengs[0].open()

class bed():
	def __init__(self,brand,size):
		self.brand = brand
		self.size = size
	def __str__(self):
		msg = ("品牌是%s\n大小是%d平方米"%(self.brand,self.size))
		return msg
	def getAred(self):
		return self.size

class esaz():
	def __init__(self,name):
		self.name = name
		self.isopen = False
	def __str__(self):
		msg = "我是%s"%self.name
		return msg
	def open(self):
		self.isopen = True
		print("灯亮了")
	def close(self):
		self.isopen = False
		print("灯灭了")
	def getIsopen(self):
		return self.isopen

myHome = Home("紫禁城1号",500)
print(myHome)
mybed = bed("席梦思",40)
print(mybed)
qxd = esaz("七星灯")
print(qxd)
myHome.addlamp(qxd)
for i in range(10):
	myHome.switch()
myHome.addBed(mybed)
myHome.addBed(mybed)
myHome.addBed(mybed)
myHome.addBed(mybed)
myHome.addBed(mybed)
myHome.addBed(mybed)
