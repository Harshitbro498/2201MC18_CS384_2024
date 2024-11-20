import pandas as pd
from collections import defaultdict
from datetime import datetime
import os

# Constants for output folder and buffer size
OUTPUT_FOLDER = "output"
BUFFER_SIZE = 5
SPARSE_MODE = 1  # 1 for Sparse; 2 for Dense

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_inputs():
    """Load input Excel files."""
    ip_1 = pd.read_excel('input/ip_1.xlsx')
    ip_2 = pd.read_excel('input/ip_2.xlsx')
    ip_3 = pd.read_excel('input/ip_3.xlsx')
    in_4 = pd.read_excel('input/in_4.xlsx')  # Roll and Name Mapping
    return ip_1, ip_2, ip_3, in_4


def generate_seating_plan(ip_1, ip_2, ip_3, buffer_size=BUFFER_SIZE, mode=SPARSE_MODE):
    """Generate seating plan (Task 1)."""
    course_student_count = ip_1['course_code'].value_counts().to_dict()

    # Sort rooms (Block 9 first, then LT)
    rooms_block_9 = ip_3[ip_3['Block'] == 9].sort_values(by='Exam Capacity', ascending=False)
    rooms_LT = ip_3[ip_3['Block'] == 'LT'].sort_values(by='Exam Capacity', ascending=False)

    # Parse exam schedule
    exam_schedule = defaultdict(lambda: {'Morning': [], 'Evening': []})
    for _, row in ip_2.iterrows():
        date = row['Date']
        morning_courses = row['Morning'].split('; ') if row['Morning'] != "NO EXAM" else []
        evening_courses = row['Evening'].split('; ') if row['Evening'] != "NO EXAM" else []
        exam_schedule[date] = {'Morning': morning_courses, 'Evening': evening_courses}

    op_1_data = []
    op_2_data = []

    for date, sessions in exam_schedule.items():
        for session, courses in sessions.items():
            courses = sorted(courses, key=lambda x: course_student_count.get(x, 0), reverse=True)
            for course in courses:
                student_rolls = ip_1[ip_1['course_code'] == course]['rollno'].tolist()
                student_index = 0
                total_students = len(student_rolls)

                for rooms in [rooms_block_9, rooms_LT]:
                    for _, room in rooms.iterrows():
                        room_capacity = room['Exam Capacity'] - buffer_size
                        max_course_seats = room_capacity // 2 if mode == 1 else room_capacity

                        allocated_students = min(total_students - student_index, max_course_seats)

                        if allocated_students > 0:
                            roll_list = ";".join(student_rolls[student_index:student_index + allocated_students])
                            op_1_data.append([date, session, course, room['Room No.'], allocated_students, roll_list])
                            student_index += allocated_students

                        if student_index >= total_students:
                            break
                    if student_index >= total_students:
                        break

    for _, room in ip_3.iterrows():
        room_no = room['Room No.']
        exam_capacity = room['Exam Capacity']
        block = room['Block']
        vacant_seats = exam_capacity - (sum(row[4] for row in op_1_data if row[3] == room_no) + buffer_size)
        op_2_data.append([room_no, exam_capacity, block, max(0, vacant_seats)])

    # Save seating plan (op_1) and room summary (op_2)
    op_1_df = pd.DataFrame(op_1_data, columns=['Date', 'Day', 'Course Code', 'Room', 'Allocated Students Count', 'Roll List'])
    op_2_df = pd.DataFrame(op_2_data, columns=['Room No.', 'Exam Capacity', 'Block', 'Vacant'])

    op_1_path = os.path.join(OUTPUT_FOLDER, 'op_1.xlsx')
    op_2_path = os.path.join(OUTPUT_FOLDER, 'op_2.xlsx')

    with pd.ExcelWriter(op_1_path) as writer:
        op_1_df.to_excel(writer, sheet_name='Seating Plan', index=False)

    with pd.ExcelWriter(op_2_path) as writer:
        op_2_df.to_excel(writer, sheet_name='Room Summary', index=False)

    return op_1_data, op_2_data


def generate_attendance_sheets(op_1_data, in_4):
    """Generate attendance sheets for Task 2."""
    roll_name_mapping = dict(zip(in_4['Roll'], in_4['Name']))  # Map roll numbers to names

    for row in op_1_data:
        date, session, course_code, room, _, roll_list = row
        
        # Convert date to string if it's a Timestamp
        if not isinstance(date, str):
            date = date.strftime('%d-%m-%Y')
        
        file_name = f"{datetime.strptime(date, '%d-%m-%Y').strftime('%d_%m_%Y')}_{course_code}_{room}_{session.lower()}.xlsx"
        file_path = os.path.join(OUTPUT_FOLDER, file_name)

        roll_numbers = roll_list.split(";")
        names = [roll_name_mapping.get(roll, "") for roll in roll_numbers]  # Fetch names using the roll number

        data = {
            'Roll No': roll_numbers,
            'Name': names,
            'Sign': ["" for _ in roll_numbers]
        }
        attendance_df = pd.DataFrame(data)

        with pd.ExcelWriter(file_path) as writer:
            attendance_df.to_excel(writer, sheet_name='Attendance', index=False)

            # Add 5 blank rows for invigilator and TA signatures
            blank_rows = pd.DataFrame([["", ""] for _ in range(5)], columns=["Invigilator", "TA"])
            blank_rows.to_excel(writer, sheet_name='Signatures', index=False)


if __name__ == "__main__":
    ip_1, ip_2, ip_3, in_4 = load_inputs()
    op_1_data, _ = generate_seating_plan(ip_1, ip_2, ip_3)
    generate_attendance_sheets(op_1_data, in_4)
    print(f"Seating plan and attendance sheets generated in {OUTPUT_FOLDER}.")
