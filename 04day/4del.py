class Dog():
	def __init__(self):
		pass
	
	def __str__(self):
		return ""

	def __del__(self):
		print("OK")

taidi = Dog()

hashiqi = taidi

del taidi
print("程序结束")
del hashiqi
