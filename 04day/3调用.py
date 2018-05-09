class Zoology():
	def call(self):
		print("吃")

class Doy(Zoology):
	def call(self):
		print("狗吃屎")
		super().call()

taidi = Doy()
taidi.call()
