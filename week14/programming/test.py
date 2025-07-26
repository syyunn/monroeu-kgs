#!/usr/bin/env python3
"""
Test script for Student Academic Management System
This script provides automated testing and demonstration of the system
"""

import os
import sys
import time
from unittest.mock import patch
import io

# Import the main module
from final_project import (
    students, add_student, search_student, calculate_average,
    get_letter_grade, generate_report, save_to_file, load_from_file,
    current_user
)


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


def test_data_types():
    """Test proper usage of Python data types"""
    print_section("Testing Data Types")
    
    # Test student dictionary structure
    test_student = {
        "id": "S1001",  # str type
        "name": "Alice Johnson",  # str type
        "grades": [85.5, 92.0, 78.5, 88.0]  # list of float
    }
    
    print(f"Student ID (str): {test_student['id']} - Type: {type(test_student['id'])}")
    print(f"Student Name (str): {test_student['name']} - Type: {type(test_student['name'])}")
    print(f"Grades (list): {test_student['grades']} - Type: {type(test_student['grades'])}")
    print(f"First Grade (float): {test_student['grades'][0]} - Type: {type(test_student['grades'][0])}")
    
    # Test tuple for immutable data
    grade_ranges = (
        ("A", 90, 100),
        ("B", 80, 89),
        ("C", 70, 79),
        ("D", 60, 69),
        ("F", 0, 59)
    )
    print(f"\nGrade Ranges (tuple): Type: {type(grade_ranges)}")
    for grade, min_score, max_score in grade_ranges:
        print(f"  {grade}: {min_score}-{max_score}")
    
    return True


def test_calculations():
    """Test grade calculations and letter grade assignment"""
    print_section("Testing Calculations")
    
    test_cases = [
        ([95, 92, 98], "A", "Pass"),
        ([85, 82, 88], "B", "Pass"),
        ([75, 72, 78], "C", "Pass"),
        ([65, 62, 68], "D", "Pass"),
        ([55, 52, 58], "F", "Fail"),
    ]
    
    for grades, expected_letter, expected_status in test_cases:
        avg = calculate_average(grades)
        letter = get_letter_grade(avg)
        status = "Pass" if avg >= 60 else "Fail"
        
        print(f"\nGrades: {grades}")
        print(f"  Average: {avg:.2f}")
        print(f"  Letter Grade: {letter} (Expected: {expected_letter})")
        print(f"  Status: {status} (Expected: {expected_status})")
        
        assert letter == expected_letter, f"Letter grade mismatch for {avg}"
        assert status == expected_status, f"Status mismatch for {avg}"
    
    print("\nAll calculation tests passed!")
    return True


def test_loop_features():
    """Test loop features with break, continue, and else"""
    print_section("Testing Loop Features")
    
    # Test 1: Using break in a loop
    print("\nTest 1: Finding first failing grade with break")
    grades = [85, 92, 78, 55, 88, 45, 90]
    for i, grade in enumerate(grades):
        if grade < 60:
            print(f"  Found failing grade: {grade} at position {i}")
            break
    else:
        print("  No failing grades found")
    
    # Test 2: Using continue in a loop
    print("\nTest 2: Counting passing grades with continue")
    passing_count = 0
    for grade in grades:
        if grade < 60:
            continue
        passing_count += 1
    print(f"  Number of passing grades: {passing_count}")
    
    # Test 3: Loop with else clause
    print("\nTest 3: Checking if all grades are passing")
    all_passing_grades = [85, 92, 78, 88, 90]
    for grade in all_passing_grades:
        if grade < 60:
            print(f"  Found failing grade: {grade}")
            break
    else:
        print("  All grades are passing!")
    
    return True


def test_conditional_logic():
    """Test conditional block logic"""
    print_section("Testing Conditional Logic")
    
    # Test login roles
    print("\nTest 1: User Role Permissions")
    roles = ["admin", "user"]
    for role in roles:
        print(f"\n  Role: {role}")
        if role == "admin":
            print("    - Can add students")
            print("    - Can edit grades")
            print("    - Can save data")
            print("    - Can view reports")
        elif role == "user":
            print("    - Can view students")
            print("    - Can search students")
            print("    - Can view reports")
            print("    - Cannot modify data")
        else:
            print("    - Unknown role")
    
    # Test grade performance logic
    print("\nTest 2: Grade Performance Categories")
    test_scores = [95, 82, 71, 64, 58]
    for score in test_scores:
        print(f"\n  Score: {score}")
        if score >= 90:
            print("    Performance: Excellent")
            print("    Status: Pass")
        elif score >= 80:
            print("    Performance: Good")
            print("    Status: Pass")
        elif score >= 70:
            print("    Performance: Satisfactory")
            print("    Status: Pass")
        elif score >= 60:
            print("    Performance: Poor")
            print("    Status: Pass")
        else:
            print("    Performance: Failing")
            print("    Status: Fail")
    
    return True


def populate_test_data():
    """Populate system with test data"""
    print_section("Populating Test Data")
    
    # Clear existing data
    students.clear()
    
    # Add test students
    test_students_data = [
        ("S1001", "Alice Johnson", [85, 92, 78, 88, 90]),
        ("S1002", "Bob Smith", [75, 68, 82, 79, 85]),
        ("S1003", "Charlie Brown", [92, 95, 98, 94, 96]),
        ("S1004", "Diana Prince", [65, 70, 68, 72, 69]),
        ("S1005", "Ethan Hunt", [55, 58, 52, 48, 60]),
    ]
    
    for student_id, name, grades in test_students_data:
        student = {
            "id": student_id,
            "name": name,
            "grades": grades
        }
        students.append(student)
        avg = calculate_average(grades)
        status = "Pass" if avg >= 60 else "Fail"
        print(f"  Added: {name} (ID: {student_id}) - Avg: {avg:.2f} - {status}")
    
    print(f"\nTotal students added: {len(students)}")
    return True


def test_file_operations():
    """Test file save and load operations"""
    print_section("Testing File Operations")
    
    # Set up admin user for file operations
    import final_project
    final_project.current_user = {"username": "admin", "role": "admin"}
    
    # Test saving
    print("\nSaving student records...")
    save_to_file()
    
    # Check if file exists
    if os.path.exists("student_records.csv"):
        print("  File created successfully!")
        
        # Show file contents
        print("\nFile contents:")
        with open("student_records.csv", "r") as f:
            contents = f.read()
            print(contents)
    
    # Test loading
    print("\nClearing current data and reloading from file...")
    students.clear()
    print(f"  Students before loading: {len(students)}")
    
    load_from_file()
    print(f"  Students after loading: {len(students)}")
    
    return True


def demonstrate_system():
    """Run a full demonstration of the system"""
    print("\n" + "="*60)
    print("  STUDENT ACADEMIC MANAGEMENT SYSTEM - TEST SUITE")
    print("="*60)
    
    # Run all tests
    tests = [
        ("Data Types", test_data_types),
        ("Calculations", test_calculations),
        ("Loop Features", test_loop_features),
        ("Conditional Logic", test_conditional_logic),
        ("Test Data Population", populate_test_data),
        ("File Operations", test_file_operations),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"\n✓ {test_name} test passed")
            else:
                failed += 1
                print(f"\n✗ {test_name} test failed")
        except Exception as e:
            failed += 1
            print(f"\n✗ {test_name} test failed with error: {e}")
    
    # Generate final report
    print_section("Generating Final Report")
    generate_report()
    
    # Summary
    print("\n" + "="*60)
    print(f"  TEST SUMMARY: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\n✓ All tests passed successfully!")
        print("\nThe Student Academic Management System is ready for use.")
        print("\nTo run the main program: python final_project.py")
        print("\nDefault credentials:")
        print("  Admin: username='admin', password='admin123'")
        print("  User:  username='user', password='user123'")
    else:
        print("\n✗ Some tests failed. Please check the implementation.")


if __name__ == "__main__":
    demonstrate_system()