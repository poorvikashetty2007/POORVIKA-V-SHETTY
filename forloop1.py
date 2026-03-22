import random
rolls = 20
count_6 = 0
count_1 = 0
two_sixes_in_row = 0
previous_roll = 0
print("Roll results:")
for i in range(rolls):
    roll = random.randint(1, 6)
    print(roll, end=" ")
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1
    previous_roll = roll
print("\n\nStatistics:")
print("Number of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Number of times two 6s occurred in a row:", two_sixes_in_row)