student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
students = 0
for student in student_heights:
    students += 1
avg_height = round(total_height / students, 2)
print(f"The average height is {avg_height}")
