input_range = int(input("Enter the input number: ")) + 1
sum = 0
for i in range (0, input_range, 2):
    sum += i
    print(f"sum is {sum}")
print(sum)