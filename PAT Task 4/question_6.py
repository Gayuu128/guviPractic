list1 = [1, 2, 3, 4, 5, 6, 8]
list2 = [4, 5, 6, 7, 8]
list3 = [0, 2, 4, 6, 8, 9]

duplicates = []

for item in list1:
    if item in list2 and item in list3:
        duplicates.append(item)

print("Duplicate elements in all three lists:", duplicates)
