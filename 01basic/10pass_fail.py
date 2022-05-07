# three subject and 33% in each subject and total marks 40%
# out of marks is taken in om (m1,m2,m3) are marks of students in subject ns is number of subject present
ns=3
om=100
m1=50
m2=50
m3=50
total=m1+m2+m3
if(total>=(40*om*ns)/100):
    if(m1>=(33*m1)/100):
        if(m2>=(33*m1)/100):
            if(m3>=(33*m1)/100):
                print("Student pass with",(100*total)/(om*ns),"%")
            else:
                print("Student Fail in subject m3")
        else:
                print("Student Fail in subject m2")
    else:
        print("Student Fail in subject m1")
else:
    print("Student Fail")                         