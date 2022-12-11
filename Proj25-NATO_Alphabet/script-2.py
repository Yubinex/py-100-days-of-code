numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 1)
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)
# 2)
result = [n for n in numbers if n % 2 == 0]
print(result)
# 3)
with open(file="Proj25-NATO_Alphabet/file1.txt") as f1:
    file_one_list = f1.readlines()
with open(file="Proj25-NATO_Alphabet/file2.txt") as f2:
    file_two_list = f2.readlines()
res = [int(num) for num in file_one_list if num in file_two_list]
print(res)
