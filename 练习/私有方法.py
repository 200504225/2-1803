class Mag():
	def __send(self,money):
		money -=10
		print("扣钱，发送成功")
	def magsend(self,money):
		if money <= 0:
			print("失败")
		else:
			self.__send(money)









mag = Mag
mag.magsend(50)
