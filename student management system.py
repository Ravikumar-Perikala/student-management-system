print('---STUDENT MANAGEMENT SYSTEM---')
print('1.Write Student')
print('2.Display Students')
print('3.Search Students')
print('4.count Students')
print('5.Exit')
choice=int(input('Enter The Choice:'))
if choice == 1:
    with open('student.txt', 'w') as s:
        n = int(input("Enter number of students: "))

        for i in range(n):
            print(f"\nEnter details for student {i + 1}")

            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            fee = input("Enter Fee: ")

            s.write(f"{student_id},{name},{course},{fee}\n")

    print("Students Written Successfully")

elif choice==2:
    with open('student.txt','r')as s:
        print(s.read())
elif choice==3:
    name=input('Enter Student Name')
    with open('student.txt','r')as s:
         n = False
         for i in s:
            if name in i:
                print('Student Found')
                print(i)
            n = True
            if n == False:
                print('Student Not Found')
elif choice==4:
    count=0
    with open('student.txt','r')as s:
        for i in s:
            count+=1
        print('Number of Students:', count)
elif choice==5:
    print('Exit\n THANK YOU')
else:
    print('Invalid Data')