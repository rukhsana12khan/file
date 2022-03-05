f=open("file88.txt","w")
s=[]
for i in range(5):
    val=input("enter")
    s.append(val+"\n")
f.writelines(s)
f.close()    