#!/usr/bin/env python3
"""
Student Academic Management System
A Python-based terminal application for managing student records
Author: Group Project
Course: KG-571, Foundation of Programming
"""

import os
import csv
import getpass
from typing import List, Dict, Optional, Tuple

# Global variables for storing data
students: List[Dict] = []
current_user: Optional[Dict] = None
users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def login_system() -> bool:
    """
    Handle user authentication
    Returns: True if login successful, False otherwise
    """
    global current_user
    print("=" * 50)
    print("Student Academic Management System - Login")
    print("=" * 50)
    
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        if username in users_db and users_db[username]["password"] == password:
            current_user = {"username": username, "role": users_db[username]["role"]}
            print(f"\nLogin successful! Welcome {username} ({current_user['role']})")
            input("\nPress Enter to continue...")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\nInvalid credentials! {attempts} attempts remaining.")
            else:
                print("\nMaximum login attempts exceeded. Exiting...")
                return False
    
    return False


def add_student():
    """Add a new student to the system"""
    if current_user["role"] != "admin":
        print("\nError: Only administrators can add students!")
        return
    
    print("\n--- Add New Student ---")
    
    # Get student information
    student_id = input("Enter Student ID (e.g., S1001): ").strip()
    
    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print(f"\nError: Student ID {student_id} already exists!")
            return
    
    name = input("Enter Student Name: ").strip()
    
    # Get grades
    grades = []
    print("\nEnter grades (press Enter without input to finish):")
    grade_count = 1
    
    while True:
        try:
            grade_input = input(f"Grade {grade_count}: ").strip()
            if grade_input == "":
                if len(grades) == 0:
                    print("At least one grade is required!")
                    continue
                else:
                    break
            
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
                grade_count += 1
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Invalid grade! Please enter a number.")
    
    # Create student record
    student = {
        "id": student_id,
        "name": name,
        "grades": grades
    }
    
    students.append(student)
    print(f"\nStudent {name} added successfully!")


def search_student():
    """Search for a student by ID or name"""
    print("\n--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by Name")
    
    choice = input("\nEnter your choice (1-2): ").strip()
    
    if choice == "1":
        search_id = input("Enter Student ID: ").strip()
        found = False
        
        for student in students:
            if student["id"] == search_id:
                display_student_details(student)
                found = True
                break
        
        if not found:
            print(f"\nNo student found with ID: {search_id}")
    
    elif choice == "2":
        search_name = input("Enter Student Name (partial match allowed): ").strip().lower()
        found_students = []
        
        for student in students:
            if search_name in student["name"].lower():
                found_students.append(student)
        
        if found_students:
            print(f"\nFound {len(found_students)} student(s):")
            for student in found_students:
                display_student_details(student)
        else:
            print(f"\nNo students found matching: {search_name}")
    else:
        print("\nInvalid choice!")


def display_student_details(student: Dict):
    """Display detailed information about a student"""
    print(f"\n{'='*40}")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Grades: {', '.join(map(str, student['grades']))}")
    
    avg = calculate_average(student['grades'])
    status = "Pass" if avg >= 60 else "Fail"
    grade_letter = get_letter_grade(avg)
    
    print(f"Average: {avg:.2f}")
    print(f"Letter Grade: {grade_letter}")
    print(f"Status: {status}")
    print(f"{'='*40}")


def calculate_average(grades: List[float]) -> float:
    """Calculate average of grades"""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def get_letter_grade(average: float) -> str:
    """Convert average to letter grade"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def view_all_students():
    """Display all student records"""
    if not students:
        print("\nNo students in the system!")
        return
    
    print("\n--- All Students ---")
    print(f"{'ID':<10} {'Name':<20} {'Average':<10} {'Status':<10} {'Grade':<5}")
    print("-" * 60)
    
    for student in students:
        avg = calculate_average(student['grades'])
        status = "Pass" if avg >= 60 else "Fail"
        grade = get_letter_grade(avg)
        
        print(f"{student['id']:<10} {student['name']:<20} {avg:<10.2f} {status:<10} {grade:<5}")


def generate_report():
    """Generate pass/fail report and statistics"""
    if not students:
        print("\nNo students to generate report!")
        return
    
    print("\n--- Grade Performance Report ---")
    
    total_students = len(students)
    passed_students = 0
    failed_students = 0
    total_average = 0
    
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for student in students:
        avg = calculate_average(student['grades'])
        total_average += avg
        
        if avg >= 60:
            passed_students += 1
        else:
            failed_students += 1
        
        letter_grade = get_letter_grade(avg)
        grade_distribution[letter_grade] += 1
    
    overall_average = total_average / total_students
    
    print(f"\nTotal Students: {total_students}")
    print(f"Passed: {passed_students} ({passed_students/total_students*100:.1f}%)")
    print(f"Failed: {failed_students} ({failed_students/total_students*100:.1f}%)")
    print(f"Overall Average: {overall_average:.2f}")
    
    print("\n--- Grade Distribution ---")
    for grade, count in grade_distribution.items():
        percentage = count / total_students * 100
        print(f"{grade}: {count} students ({percentage:.1f}%)")


def save_to_file():
    """Save student records to CSV file"""
    if current_user["role"] != "admin":
        print("\nError: Only administrators can save data!")
        return
    
    if not students:
        print("\nNo data to save!")
        return
    
    filename = "student_records.csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Grades"])
            
            for student in students:
                grades_str = ";".join(map(str, student['grades']))
                writer.writerow([student['id'], student['name'], grades_str])
        
        print(f"\nData saved successfully to {filename}")
    except Exception as e:
        print(f"\nError saving file: {e}")


def load_from_file():
    """Load student records from CSV file"""
    global students
    filename = "student_records.csv"
    
    if not os.path.exists(filename):
        print(f"\nFile {filename} not found!")
        return
    
    try:
        loaded_students = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                grades = [float(g) for g in row['Grades'].split(';')]
                student = {
                    "id": row['ID'],
                    "name": row['Name'],
                    "grades": grades
                }
                loaded_students.append(student)
        
        students = loaded_students
        print(f"\nLoaded {len(students)} student records from {filename}")
    except Exception as e:
        print(f"\nError loading file: {e}")


def edit_grades():
    """Edit student grades"""
    if current_user["role"] != "admin":
        print("\nError: Only administrators can edit grades!")
        return
    
    print("\n--- Edit Student Grades ---")
    student_id = input("Enter Student ID: ").strip()
    
    student = None
    for s in students:
        if s["id"] == student_id:
            student = s
            break
    
    if not student:
        print(f"\nStudent ID {student_id} not found!")
        return
    
    display_student_details(student)
    
    print("\n1. Add new grade")
    print("2. Edit existing grade")
    print("3. Delete grade")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        try:
            new_grade = float(input("Enter new grade: "))
            if 0 <= new_grade <= 100:
                student["grades"].append(new_grade)
                print("\nGrade added successfully!")
            else:
                print("\nGrade must be between 0 and 100!")
        except ValueError:
            print("\nInvalid grade!")
    
    elif choice == "2":
        if not student["grades"]:
            print("\nNo grades to edit!")
            return
        
        print("\nCurrent grades:")
        for i, grade in enumerate(student["grades"]):
            print(f"{i+1}. {grade}")
        
        try:
            index = int(input("\nEnter grade number to edit: ")) - 1
            if 0 <= index < len(student["grades"]):
                new_grade = float(input("Enter new grade: "))
                if 0 <= new_grade <= 100:
                    student["grades"][index] = new_grade
                    print("\nGrade updated successfully!")
                else:
                    print("\nGrade must be between 0 and 100!")
            else:
                print("\nInvalid grade number!")
        except ValueError:
            print("\nInvalid input!")
    
    elif choice == "3":
        if not student["grades"]:
            print("\nNo grades to delete!")
            return
        
        print("\nCurrent grades:")
        for i, grade in enumerate(student["grades"]):
            print(f"{i+1}. {grade}")
        
        try:
            index = int(input("\nEnter grade number to delete: ")) - 1
            if 0 <= index < len(student["grades"]):
                if len(student["grades"]) > 1:
                    deleted_grade = student["grades"].pop(index)
                    print(f"\nGrade {deleted_grade} deleted successfully!")
                else:
                    print("\nCannot delete the only grade!")
            else:
                print("\nInvalid grade number!")
        except ValueError:
            print("\nInvalid input!")


def main_menu():
    """Display main menu and handle user choices"""
    while True:
        clear_screen()
        print("=" * 50)
        print("Student Academic Management System")
        print(f"Logged in as: {current_user['username']} ({current_user['role']})")
        print("=" * 50)
        
        print("\n1. Add Student (Admin only)")
        print("2. Search Student")
        print("3. View All Students")
        print("4. Edit Grades (Admin only)")
        print("5. Generate Report")
        print("6. Save to File (Admin only)")
        print("7. Load from File")
        print("8. Logout")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            edit_grades()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "8":
            print("\nLogging out...")
            return "logout"
        elif choice == "9":
            print("\nThank you for using Student Academic Management System!")
            return "exit"
        else:
            print("\nInvalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


def main():
    """Main program entry point"""
    print("Welcome to Student Academic Management System")
    print("=" * 50)
    
    # Attempt to load existing data
    if os.path.exists("student_records.csv"):
        print("\nFound existing student records. Loading...")
        load_from_file()
        input("\nPress Enter to continue...")
    
    # Main program loop
    while True:
        clear_screen()
        
        # Login
        if not login_system():
            break
        
        # Run main menu
        result = main_menu()
        
        if result == "exit":
            break
        elif result == "logout":
            global current_user
            current_user = None
            continue


if __name__ == "__main__":
    main()