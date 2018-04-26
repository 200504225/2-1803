na = input("请输入文件名字加后缀")
f = open(na,"r")

po = na.rfind(".")
i = na[0:po]
j = na[po:]

name = open(i+"备份"+j,"w")
while True:
	co = f.read(2)
	if len(co) ==0:
		break
	name.write(co)
f.close()
name.close()
