f=open("file.txt","r")
str="_"
while str:
    str=f.readline()
    print(str)
f.close()    
