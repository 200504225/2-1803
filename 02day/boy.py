class Boy():
	def __init__(self,age,wright):
		self.age = age
		self.wright = wright
		self.game = []
		for i in range(3):
			game = input("请输入游戏")
			self.game.append(game)
	def sleep(self):
		print("睡觉")
	def peas(self):
		print("打豆豆")
	def game(self):
		for i in self.game:
			print(i)
	def ego(self):
		print("年龄是%s\n体重是%s\n喜欢的游戏%s\n"%(self.age,self.wright,i))
laowang = Boy(20,80)
laowang.sleep()
laowang.peas()
laowang.ego()
