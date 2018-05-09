class Mag():
	def __markMag(self,money):
		money -= 1
		print("发送成功")

	def pull(self,money):
		if money <= 0:
			print("余额不足")
		else:
			self.__markMag(money)



mag = Mag()
mag.pull(10)
