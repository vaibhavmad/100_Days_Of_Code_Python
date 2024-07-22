user_permission = "y"
student_score = []
while user_permission != "n":
    student_score.append(int(input("Enter the score one by one: \n")))
    user_permission = input("Do you want to add more data? 'y' and enter for yes, 'n' to stop and calculate the highest:")

high_score = 0
counter = 0
for i in student_score:
    if high_score < student_score[counter]:
        high_score = student_score[counter]
    counter += 1

print(f"highest score is: {high_score}")
