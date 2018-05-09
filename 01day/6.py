'''
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
'''

file_name = input("请输入文件的名字要带后缀名")
old_file = open(file_name,'r')

#1.txt--->1复制.txt
#1.txt.txt

position = file_name.rfind(".")
new_file_name = file_name[0:position]+"备份"+file_name[position:]
new_file = open(new_file_name,'w')

while True:
	content = old_file.read(1024)
	
	if len(content) == 0:
		break

	new_file.write(content)

old_file.close()
new_file.close()
