#The range is 1-100, so the loop must end at 101
END_OF_RANGE = 101 
final_sum = 0
for current_number in range(1, END_OF_RANGE):
    final_sum += current_number
print(final_sum)