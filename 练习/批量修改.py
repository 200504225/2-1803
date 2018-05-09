import os
name = input("请输入添加的文件夹名")
list = os.listdir(name)#以列表的形式取出文件夹的文件
for i in list:
	po = i.rfind(".")#取需要插入的位置
	x_name = i[0:po]+"老年人"+i[po:]#"老年人"为需要添加的值
	os.chdir("/home/xuedongyan/桌面/2-1803/练习/游戏")#更改默认目录
	os.rename(i,x_name)

