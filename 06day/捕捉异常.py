try:

	print(God)
	11/0
except SyntaxError:
	print("?") 
except Exception as ll:
	print("出错了")
	print(ll)

