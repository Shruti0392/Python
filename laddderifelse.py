rno=int(input ("Enter Roll No :"))
sname=input("Enter Student Name : ")
s1=int(input("Enter Marks of subject 1 : "))
s2=int(input("Enter Marks of subject 2 : "))
s3=int(input("Enter Marks of Subject 3 : "))


total=s1+s2+s3
per=total/3


print("Roll NO : ",rno)
print("Student Name : ",sname)
print("Total : ",total)
print("percentage :",per)

        
if per>=70:
        print("Distinction")
if per>=60:
        print("First class")
if per>=50:
        print("Second class")
elif per>=40:
        print("Pass class")
else:
      print("FAIL")
