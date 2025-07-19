from main import *

print("Testing Student Academic Management System")
print("="*50)

students.clear()

print("\n1. Testing add_student function")
students.append({'id': 'S1001', 'name': 'Alice Johnson', 'grades': []})
students.append({'id': 'S1002', 'name': 'Bob Smith', 'grades': []})
students.append({'id': 'S1003', 'name': 'Charlie Brown', 'grades': []})
print(f"Added {len(students)} students")

print("\n2. Testing update_grades function")
students[0]['grades'] = [85, 78, 92]
students[1]['grades'] = [90, 80, 85]
students[2]['grades'] = [45, 52, 48]
print("Grades added for all students")

print("\n3. Testing calculate_average function")
for student in students:
    avg = calculate_average(student['grades'])
    print(f"{student['name']}: Average = {avg:.2f}")

print("\n4. Testing search functionality")
print("Searching for student with ID 'S1002':")
for student in students:
    if student['id'] == 'S1002':
        print(f"Found: {student['name']} - Grades: {student['grades']}")

print("\n5. Testing report generation")
generate_report()

print("\n6. Testing file operations")
print("Saving to test_data.csv...")
with open('test_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Grades'])
    for student in students:
        grades_str = ';'.join(map(str, student['grades']))
        writer.writerow([student['id'], student['name'], grades_str])
print("File saved successfully!")

print("\nAll tests completed successfully!")