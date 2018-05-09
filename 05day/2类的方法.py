class Date():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day

	def openDate(self):
		print("%s年%s月%s日"%(self.year,self.month,self.day))


	@classmethod
	def xDote(cls,ll):
		a,b,c = ll.split("-")
		d = cls(a,b,c)
		return d
d = Date("2081","05","06")
d.openDate()

str ="2018-05-06"
Date.xDote(str).openDate()

