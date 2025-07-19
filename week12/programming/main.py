import os
import csv

students = []

def add_student():
    while True:
        student_id = input("Enter student ID (or 'done' to finish): ").strip()
        if student_id.lower() == 'done':
            break
        
        name = input("Enter student name: ").strip()
        
        if not student_id or not name:
            print("Error: ID and name cannot be empty.")
            continue
        
        for student in students:
            if student['id'] == student_id:
                print(f"Error: Student with ID {student_id} already exists.")
                break
        else:
            student = {'id': student_id, 'name': name, 'grades': []}
            students.append(student)
            print(f"Student {name} (ID: {student_id}) added successfully!")

def search_student():
    search_type = input("Search by (1) ID or (2) Name? Enter 1 or 2: ").strip()
    
    if search_type == '1':
        student_id = input("Enter student ID: ").strip()
        for student in students:
            if student['id'] == student_id:
                print(f"\nFound: ID: {student['id']}, Name: {student['name']}")
                if student['grades']:
                    print(f"Grades: {student['grades']}")
                    print(f"Average: {calculate_average(student['grades']):.2f}")
                else:
                    print("No grades recorded yet.")
                return
        print(f"No student found with ID: {student_id}")
    
    elif search_type == '2':
        name = input("Enter student name: ").strip().lower()
        found = False
        for student in students:
            if name in student['name'].lower():
                print(f"\nFound: ID: {student['id']}, Name: {student['name']}")
                if student['grades']:
                    print(f"Grades: {student['grades']}")
                    print(f"Average: {calculate_average(student['grades']):.2f}")
                else:
                    print("No grades recorded yet.")
                found = True
        if not found:
            print(f"No student found with name containing: {name}")
    else:
        print("Invalid option. Please enter 1 or 2.")

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def update_grades():
    student_id = input("Enter student ID to update grades: ").strip()
    
    for student in students:
        if student['id'] == student_id:
            print(f"Updating grades for {student['name']} (ID: {student['id']})")
            print("Current grades:", student['grades'])
            
            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ").strip()
                if grade_input.lower() == 'done':
                    break
                
                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        student['grades'].append(grade)
                        print(f"Grade {grade} added successfully!")
                    else:
                        print("Error: Grade must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid number.")
            
            if student['grades']:
                print(f"Updated grades: {student['grades']}")
                print(f"New average: {calculate_average(student['grades']):.2f}")
            return
    
    print(f"No student found with ID: {student_id}")

def generate_report():
    if not students:
        print("No students in the system.")
        return
    
    passing_grade = 60
    passed = 0
    failed = 0
    no_grades = 0
    
    print("\n" + "="*50)
    print("STUDENT ACADEMIC REPORT")
    print("="*50)
    
    for student in students:
        print(f"\nStudent: {student['name']} (ID: {student['id']})")
        
        if not student['grades']:
            print("Status: No grades recorded")
            no_grades += 1
        else:
            avg = calculate_average(student['grades'])
            status = "PASS" if avg >= passing_grade else "FAIL"
            print(f"Grades: {student['grades']}")
            print(f"Average: {avg:.2f}")
            print(f"Status: {status}")
            
            if avg >= passing_grade:
                passed += 1
            else:
                failed += 1
    
    print("\n" + "-"*50)
    print("SUMMARY")
    print(f"Total Students: {len(students)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"No Grades: {no_grades}")
    print("="*50)

def save_to_file():
    filename = input("Enter filename to save (without extension): ").strip()
    if not filename:
        filename = "student_records"
    
    filename += ".csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Grades'])
            
            for student in students:
                grades_str = ';'.join(map(str, student['grades']))
                writer.writerow([student['id'], student['name'], grades_str])
        
        print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file():
    filename = input("Enter filename to load (without extension): ").strip()
    if not filename:
        filename = "student_records"
    
    filename += ".csv"
    
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        return
    
    try:
        loaded_count = 0
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                if len(row) >= 3:
                    student_id = row[0]
                    name = row[1]
                    grades_str = row[2]
                    
                    grades = []
                    if grades_str:
                        grades = [float(g) for g in grades_str.split(';')]
                    
                    exists = False
                    for student in students:
                        if student['id'] == student_id:
                            exists = True
                            break
                    
                    if not exists:
                        students.append({
                            'id': student_id,
                            'name': name,
                            'grades': grades
                        })
                        loaded_count += 1
        
        print(f"Successfully loaded {loaded_count} student(s) from {filename}")
    except Exception as e:
        print(f"Error loading file: {e}")

def display_all_students():
    if not students:
        print("No students in the system.")
        return
    
    print("\n" + "="*50)
    print("ALL STUDENTS")
    print("="*50)
    
    for student in students:
        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        if student['grades']:
            print(f"Grades: {student['grades']}")
            print(f"Average: {calculate_average(student['grades']):.2f}")
        else:
            print("Grades: No grades recorded")
    print("="*50)

def main():
    print("="*50)
    print("STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("="*50)
    
    while True:
        print("\nMAIN MENU")
        print("1. Add New Student")
        print("2. Search Student")
        print("3. Update Student Grades")
        print("4. Generate Report")
        print("5. Display All Students")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            update_grades()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            save_to_file()
        elif choice == '7':
            load_from_file()
        elif choice == '8':
            print("\nThank you for using the Student Academic Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()