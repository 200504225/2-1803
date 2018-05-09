name = open("1.txt","r")
go = name.read()
name1 = "1.txt"
ke = name1.rfind(".")
x_name = name1[0:ke]+"备份"+name1[ke:]
x_go = open(x_name,"w")
x_go.write(go)

name.close()
x_go.close()
