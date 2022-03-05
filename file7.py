f=open("file.txt","r")
str="_"
length=0
size=0
while str:
    str=f.readline()
    length=length+len(str)
    size=size+len(str.strip())
print(length)
print(size) 
f.close()  