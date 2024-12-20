def calculate_average(student):
    subjects = ['math', 'english', 'science']
    return (student['math'] + student['english'] + student['science']) / 3
def assess_performance(student):
    average_grade = calculate_average(student)
    if average_grade >= 90 and student['attendance'] >= 90:
        return 'Excellent'
    elif average_grade >= 70 and student['attendance'] >= 80:
        return 'Good'
    elif average_grade >= 50 and student['attendance'] >= 70:
        return 'Needs Improvement'
    else:
        return 'Failing'
def get_student_data():
    students = []
    num_students = int(input("Enter the number of students: "))
    
    for _ in range(num_students):
        name = input("Enter student name: ")
        math = float(input("Enter math score: "))
        english = float(input("Enter English score: "))
        science = float(input("Enter science score: "))
        attendance = int(input("Enter attendance percentage: "))
        behavior = input("Enter behavior: ")
        
        student = {
            'name': name,
            'math': math,
            'english': english,
            'science': science,
            'attendance': attendance,
            'behavior': behavior
        }
        students.append(student)
    
    return students
students_data = get_student_data()
print(f"{'Name':<10}{'Average Grade':<15}{'Attendance':<12}{'Behavior':<15}{'Performance':<15}")
print("-" * 70)

for student in students_data:
    average = calculate_average(student)
    performance = assess_performance(student)
    print(f"{student['name']:<10}{average:<15.2f}{student['attendance']:<12}{student['behavior']:<15}{performance:<15}")