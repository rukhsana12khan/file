banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("listaddfile.txt","w")
for i in banks_list:
    file.write(i+"\n") 

file.close()
