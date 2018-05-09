class pig():
	def eat(self):
		print("吃货")
	def sleep(self):
		print("睡觉")
	def introduce(self):
		print("我是%s\n我有%s\n我的皮肤%s\n"%(self.name,self.allfours,self.hair))#self 谁调用代表谁

hog = pig()
hog.allfours = "四条腿"
hog.hair = "毛发稀疏"
hog.name = "家猪"
hog.eat()
hog.sleep()
hog.introduce()


