import pandas as pd

data = pd.read_csv("Proj24-US_States/weather_data.csv")

"""
print(data["temp"].mean())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# get specific value of row
monday = data[data.day == "Monday"]
print(monday.condition)
"""

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)  # type: ignore
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pd.DataFrame(data_dict)
data.to_csv("Proj24-US_States/new_data.csv")
