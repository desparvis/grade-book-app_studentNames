#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0
        total_credits = sum(course['credits'] for course in self.courses_registered)
        total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
        self.GPA = total_points / total_credits
        return self.GPA

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        print(f"Student {names} added.")

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"Course {name} added.")

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            print(f"Student {student_email} registered for {course_name}.")
        else:
            print("Error: Student or course not found.")

    def calculate_GPA(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            gpa = student.calculate_GPA()
            print(f"GPA for {student_email} is {gpa:.2f}")
        else:
            print("Error: Student not found.")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        print("\nStudent Rankings:")
        for rank, student in enumerate(self.student_list, start=1):
            print(f"{rank}. {student.names} ({student.email}) - GPA: {student.GPA:.2f}")

    def search_by_grade(self, grade_min, grade_max):
        filtered_students = [s for s in self.student_list if grade_min <= s.GPA <= grade_max]
        print("\nStudents with GPA between", grade_min, "and", grade_max, ":")
        for student in filtered_students:
            print(f"{student.names} ({student.email}) - GPA: {student.GPA:.2f}")

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print("\nTranscript for", student.names, ":")
            print("Email:", student.email)
            print("GPA:", student.GPA)
            print("Courses:")
            for course in student.courses_registered:
                print(f"{course['course'].name}: Grade {course['grade']}, Credits {course['credits']}")
        else:
            print("Error: Student not found.")

def main():
    gradebook = GradeBook()

    while True:
        print("\n--- Grade Book Application ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = float(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)

        elif choice == '4':
            student_email = input("Enter student email: ")
            gradebook.calculate_GPA(student_email)

        elif choice == '5':
            gradebook.calculate_ranking()

        elif choice == '6':
            grade_min = float(input("Enter minimum grade: "))
            grade_max = float(input("Enter maximum grade: "))
            gradebook.search_by_grade(grade_min, grade_max)

        elif choice == '7':
            student_email = input("Enter student email: ")
            gradebook.generate_transcript(student_email)

        elif choice == '8':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

