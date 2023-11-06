records = {
    'name': "list of student records",
    'data': [
        {'name': 'Manjeet', 'marks': [1, 4, 5, 6]},
        {'name': 'Akash', 'marks': [1, 8, 9]},
        {'name': 'Nikhil', 'marks': [10, 22, 4]},
        {'name': 'Deborah', 'marks': [22, 11, 9]}
    ]
}

print("Before removing duplicates:")
print(records)

# Create a set to store unique marks across all students
unique_marks = []
# Create a set to store duplicate marks
duplicate_marks = []



for student in records['data']:
    student_marks = student['marks']
    unique_student_marks = []
    
    for mark in student_marks:
        if mark not in unique_marks:
            unique_marks.append(mark)
            unique_student_marks.append(mark)
        else:
            duplicate_marks.append(mark)
    
    student['marks'] = unique_student_marks
    #print (unique_student_marks)
            

# Remove duplicate marks from all students
for student in records['data']:
    student['marks'] = [x for x in student['marks'] if x not in duplicate_marks]

print("\nAfter removing Duplicates:")
print(records)