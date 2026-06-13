Student={}

while True:
    print("\n----student management system----")
    print("1. add student")
    print("2. View student")
    print("3. Check Result")  
    print("4. Exit")


    choice = input("Enter your choice:")

    if choice == '1':
        name = input("Enter student name:")
        marks = input("Enter student marks:")
        Student[name] = marks
        print("Student added successfully!")



    elif choice == '2':
        if not Student:
            print("No students found.")
        else:
            print("Student List:")
            for name, marks in Student.items():
                print(f"Name: {name}, Marks: {marks}")     


    elif choice == '3':
        name = input("Enter student name to check result:")
        if name in Student:
            marks = Student[name]

            if marks >= '40':
                print(f"{name} has passed.")
            else:
                print(f"{name} has failed.")

        else:
            print("Student not found.")


    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break   


    else:
        print("Invalid choice. Please try again.")
