f=open("file88.txt","w")
for i in range(5):
    name=input("enter")
    f.write(name)
    f.write('\n')
f.close()