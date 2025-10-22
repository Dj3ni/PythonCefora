
list_students = {
    "bob" : ["Bob", "Morane", 25 , "Python"],
    "tom" : ["Tom", "Sauwyer", 25 , "Javascript"],
    "shirley" : ["Shirley", "Temple", 85 , "Sql"]
}
choice = ""

while choice != "q":
    print("1 - Diplay the students list")
    print("2 - Add a student")
    print("3 - Remove a student")

    choice = input("Select your option: ")

    match choice:
        case "1":
            print("Diplay the students list: ")
            for key, value in list_students.items():
                print(f"{key} : {value}")
        case "2":
            print("Add a student: ")
            user_info = []

            user_info.append(input("Enter your firstname: "))
            user_info.append(input("Enter your lastname: "))
            user_info.append(input("Enter your age: "))
            user_info.append(input("Enter your course: "))
        case "3":
            print("Remove a student: ")
            student_to_remove = input("Enter the student to remove: ")
            list_students.pop(student_to_remove)
