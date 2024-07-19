list_1 = ["#", "#", "#"]
list_2 = ["#", "#", "#"]
list_3 = ["#", "#", "#"]

map = [list_1, list_2, list_3]
print("Here's the map: ")
print(f"{list_1} \n{list_2} \n{list_3}")
treasure_location = input("Where do you want to put the treaure?: ")

cols = ["a", "b", "c"]
col_num = cols.index(treasure_location[0])
row_num = int(treasure_location[1])
map[row_num-1][col_num] = "X"

print("Your treasure is now secure in vault")
print(f"{list_1} \n{list_2} \n{list_3}")