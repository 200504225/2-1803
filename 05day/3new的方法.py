class Dog():
	def __init__(self):
		print("ヾ(￣▽￣)Bye~Bye~\n")
	def __str__(self):
		print("♪(^∇^*)\n")
	def __del__(self):
		print("O(∩_∩)O哈哈~\n")
	def __new__(cls):
		print("~~~~(>_<)~~~~\n")
		return object.__new__(cls)
		
Dog()
