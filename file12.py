batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul88.html", "w")
for student in batch1_students:
    students_file.write( student+"\n")
students_file.close()