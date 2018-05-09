class ShowError(Exception):
	def __init__(self,length,lento):
		self.length = length
		self.lento = lento

def main():
	try:
		s = input("请输入")
		if len(s)<3:
			raise ShowError(len(s),3)
	except ShowError as result:
		print("输入的长度是%d,长度需要%d"%(result.length,result.lento))
	else:
		print("没有异常")

main()
