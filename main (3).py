class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [Student("Alice", "A123", 3.8), Student("Bob", "B456", 3.5), Student("Charlie", "C789", 3.9)]
students2 = [Student("Eva", "E321", 3.6), Student("David", "D654", 3.2), Student("Fiona", "F987", 4.0)]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

# Print sorted student lists
print("Sorted students list 1:")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

print("\nSorted students list 2:")
for student in sorted_students2:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")