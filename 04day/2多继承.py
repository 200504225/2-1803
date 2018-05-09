class A():
	def tes(self):
		print("------A-------")
class B():
	def tes(self):
		print("------B-------")
class C(A,B):
	pass


c =	C()
c.tes()

