import os
name = input("请输入文件名")
j = os.listdir(name)
for i in j:
	po = i.rfind(".")
	x_name = i[0:po]+"炎"+i[po:]
	os.chdir("/home/xuedongyan/桌面/2-1803/01day/游戏")
	os.rename(i,x_name)
