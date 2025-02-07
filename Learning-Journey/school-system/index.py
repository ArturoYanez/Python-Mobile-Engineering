import random

# List of names
names = [
        "JA", "MC", "LM", "AB",
        "CD", "EF", "GH", "IJ",
        "KL", "MN", "OP", "QR",
        "ST", "UV", "WX", "YZ",
        "PQ", "RS", "TU"
]

records = []


# Generate Random Attendance
def generate_attendance(days=30):
    attendance = []
    for i in range(days):
        attendance.append(random.choice(['P', 'A']))
    return attendance


# Attendance records for each student
def record_attendance(names):
    for i in range(len(names)):
        record = [names[i], generate_attendance(30)]
        records.append(record)
    return records


# Calculate and Evaluate Attendance
def calculate_and_evaluate_attendance(records):
    for record in records:
        absencesTotal = record[1].count('A')
        if absencesTotal >= len(record[1]) * 0.55:  # 55% attendance allowed
            result = 'REPROBADO'
        else:
            result = 'APROBADO'
        record.append(result)  # Add results
    return records


# Execute functions
record_attendance(names)
final_records = calculate_and_evaluate_attendance(records)

# Print Final Results
for record in final_records:
    print(f'''
          Student: {record[0]},
          Attendance: {record[1]},
          Result: {record[2]}
          ''')
