# *Attendance Registration System*

## *Description*
This Python project provides a simple solution for student attendance registration over a month, in the context of a contingency where the main registration system is out of service. The system allows for:
 * *Attendance Registration* : Enter student initials and mark their presence (P) or absence (A) for each day.
 * *Attendance Calculation* : At the end of the period, the system calculates the total number of presences and absences for each student.
 * *Attendance Evaluation* : Determines if a student passes or fails based on a maximum limit of 10% absences per semester.

## *Requirements*
 * *Python* : Latest stable version.

## *Usage*
 * *Run the script* :
   ```sh
   python attendance_registration.py
   ```

## *Enter data* :
   Follow the program's prompts to enter student initials and their respective attendances.

## *View results* :
   At the end, the program will display a summary of each student's attendance, including the number of presences, absences, and the final result (passed or failed).

## *Code Structure*
 * `attendance_registration.py`: Contains the main program logic, including functions to:
   * Create a list of students.
   * Register each student's attendance.
   * Calculate the attendance percentage.
   * Evaluate if a student passes or fails.
   * Display the final results.

## *Considerations*
 * *Simplification* : This project assumes that all students have the same number of classes during the month.
 * *Expansion* : The system can be expanded to include multiple groups of students, different types of evaluations, and more detailed reports.

## *Example*
```python
# attendance_registration.py

students = ["JA", "MC", "LM", ...]  # List of students (initials)
...  # Rest of the code
```