class Date():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def open(self):
		print("%s年%s月%s日"%(self.year,self.month,self.day))

	@classmethod
	def openDate(cls,str):
		a,b,c = str.split("-")
		b = cls(a,b,c)
		return b




str = "2018-06-09"
Date.openDate(str).open()
