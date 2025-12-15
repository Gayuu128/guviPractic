numbers = [4, 2, -3, 1, 6]

found = False

for start in range(len(numbers)):
    curr_sum = 0
    for end in range(start, len(numbers)):
        curr_sum += numbers[end]
        if curr_sum == 0:
            print("Sub-list with sum 0 found:", numbers[start:end+1])
            found = True

if not found:
    print("No sub-list with sum 0 found")
