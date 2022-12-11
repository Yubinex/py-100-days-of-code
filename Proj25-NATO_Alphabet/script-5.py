import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
""" for (key, value) in student_data_frame.items():
    print(key)
    print(value) """

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    print(row.score)
