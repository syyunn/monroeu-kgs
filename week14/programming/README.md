# Student Academic Management System

## System Design and Flow

### Overview
The Student Academic Management System is a Python-based terminal application designed for academic staff to manage student records efficiently. The system provides comprehensive functionality for student registration, grade management, analytics, and reporting.

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Login System                          │
│              (Authentication Layer)                     │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                   Main Menu                             │
│            (User Interface Layer)                       │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│              Core Functions                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ Add Student │  │Search Student│  │View Students│    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ Edit Grades │  │Generate Report│ │File Operations│  │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
└─────────────────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│                  Data Layer                             │
│         (In-Memory Storage + CSV Files)                 │
└─────────────────────────────────────────────────────────┘
```

### Data Structure

The system uses Python dictionaries and lists to store student information:

```python
student = {
    "id": "S1001",         # String: Unique identifier
    "name": "Alice Johnson", # String: Student name
    "grades": [85, 92, 78]  # List of floats: Grade scores
}

students = [student1, student2, ...]  # List of all students
```

### Key Features

#### 1. **Authentication System**
- **Login Credentials:**
  - Admin: username='admin', password='admin123'
  - User: username='user', password='user123'
- **Role-based Access:**
  - Admin: Full access (add, edit, delete, save)
  - User: Read-only access (view, search, reports)
- **Security Features:**
  - Password masking using getpass
  - Maximum 3 login attempts
  - Session management

#### 2. **Student Management**
- **Add Student** (Admin only)
  - Unique ID validation
  - Name entry
  - Multiple grade entry with validation (0-100)
  
- **Search Functionality**
  - Search by ID (exact match)
  - Search by name (partial match, case-insensitive)
  
- **View Options**
  - Individual student details
  - All students in tabular format
  - Automatic grade calculations

#### 3. **Grade Analysis**
- **Automatic Calculations:**
  - Average grade computation
  - Letter grade assignment (A-F)
  - Pass/Fail status (60% threshold)
  
- **Grade Scale:**
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: 0-59

#### 4. **Reporting System**
- **Statistics Generated:**
  - Total students count
  - Pass/fail percentages
  - Overall class average
  - Grade distribution by letter
  
- **Visual Formatting:**
  - Tabular data display
  - Percentage calculations
  - Distribution charts

#### 5. **File Operations**
- **Save to CSV:**
  - Exports all student records
  - Preserves data structure
  - Admin-only functionality
  
- **Load from CSV:**
  - Imports existing records
  - Auto-loads on startup if file exists
  - Data validation during import

### Program Flow

1. **Startup**
   - Check for existing data file
   - Load data if available
   - Display welcome message

2. **Authentication**
   - Request username/password
   - Validate credentials
   - Set user role and permissions

3. **Main Loop**
   - Display menu based on user role
   - Process user selection
   - Execute selected function
   - Return to menu or logout

4. **Data Operations**
   - All operations validate input
   - Changes are kept in memory
   - Save explicitly writes to file

### Control Structures

#### Conditional Logic
- **Login System:** Multi-level authentication with role checking
- **Grade Performance:** Nested conditions for grade classification
- **Menu Options:** Role-based menu item availability

#### Loop Implementation
- **Main Program Loop:** While loop with break for exit
- **Grade Entry:** Loop with continue for validation
- **Search Results:** For loop with else clause for no matches

### Error Handling
- Input validation for all user entries
- Graceful handling of file operations
- Clear error messages for user guidance
- Prevention of data corruption

### Testing

Run the test suite to verify all functionality:

```bash
python test.py
```

The test suite covers:
- Data type usage verification
- Calculation accuracy
- Loop feature demonstration
- Conditional logic testing
- File operation validation
- Complete system integration

### Usage Instructions

1. **Run the main program:**
   ```bash
   python final_project.py
   ```

2. **Login with credentials:**
   - Admin access: admin/admin123
   - User access: user/user123

3. **Navigate using menu numbers**

4. **Save data before exiting** (Admin only)

### Technical Requirements Met

✓ **Data Types:** Proper use of int, float, list, tuple, str  
✓ **Conditional Logic:** Complex if/elif/else structures  
✓ **Loops:** Implementation of for/while with break, continue, else  
✓ **Functions:** Modular design with clear responsibilities  
✓ **File Handling:** CSV read/write operations  
✓ **Documentation:** Comprehensive inline comments  
✓ **User Interface:** Clear terminal-based interaction  
✓ **Security:** Role-based access control  
✓ **Error Handling:** Graceful error management  
✓ **Analytics:** Statistical calculations and reporting