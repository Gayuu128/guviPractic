numbers = [4, 5, 1, 2, 5, 1, 4, 3, 2]

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break
