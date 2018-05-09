class ShowError(Exception):
	def __init__(self,len,lee):
		self.len = len
		self.lee = lee


def main():
	try:
		s = input("请输入")
		if len(s)<3:
			raise ShowError(len(s),3)
	except ShowError as ll:
		print("你传的长度为%d，需要的长度是%d"%(ll.len,ll.lee))

main()
		
