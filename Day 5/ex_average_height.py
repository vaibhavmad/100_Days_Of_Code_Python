user_permission = "y"
students_height = []
while user_permission != "n":
    students_height.append(int(input("Enter the height of the individual student in cms: \n")))
    user_permission = input("Do you want to add more data? 'y' and enter for yes, 'n' to stop and calculate the average:")


count_list = len(students_height)
height = 0
for i in students_height:
    height += i
print(f"Total students added: {count_list}")
print(f"The average height of this class is: {round(height/len(students_height))} cms.")
