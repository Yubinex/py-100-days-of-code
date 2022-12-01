row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n> ")

map[int(position[0])-1][int(position[1])-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
