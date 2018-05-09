class Msg():
	def __send(self,money):
		money -= 10
		print("扣钱，成功发送信息")
	def getsend(self,money):
		if money <= 0:
			print("失败")
		else:
			self.__send(money)


mgs = Msg()
mgs.getsend(50)
