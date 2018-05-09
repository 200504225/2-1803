class Dog():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day

	def open(self):
		print("%s年%s月%s日"%(self.year,self.month,self.day))


	@classmethod
	def method(cls,ll):
		a,b,c = ll.split("-")
		b = cls(a,b,c)
		return b




str = "2018-05-06"
Dog.method(str).open()
