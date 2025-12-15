numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_count = 0
happy_numbers = []

for num in numbers:
    n = num
    visited = []

    while n != 1 and n not in visited:
        visited.append(n)
        sum_sq = 0

        for digit in str(n):
            sum_sq = sum_sq + int(digit) * int(digit)

        n = sum_sq

    if n == 1:
        happy_numbers.append(num)
        happy_count = happy_count + 1

print("Happy Numbers:", happy_numbers)
print("Count of Happy Numbers:", happy_count)
