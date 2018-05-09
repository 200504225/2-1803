class mutton():
	def __init__(self):
		self.baketime = 0
		self.ripe = "生"

		self.list = []
	def __str__(self):
		return self.ripe
	def sea(self,se):
		self.list.append(se)
	def bake(self,time):
		self.baketime+=time
		if self.baketime > 0 and self.baketime < 4:
			self.ripe = "半生不熟"
		elif self.baketime >= 4 and self.baketime <8:
			self.ripe = "八分熟了"
		elif self.baketime >= 8:
			self.ripe = "焦了"
bak = mutton()
bak.bake(1)
bak.sea("辣椒")
print(bak)
bak.bake(1)
print(bak)
bak.bake(1)
print(bak)
bak.bake(1)
print(bak)
bak.bake(1)
print(bak)
bak.bake(1)
print(bak)
bak.bake(1)
print(bak)
