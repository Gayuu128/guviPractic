num = int(input("Enter an integer: "))

num = abs(num)   # to handle negative numbers

last_digit = num % 10

while num >= 10:
    num = num // 10

first_digit = num

sum_digits = first_digit + last_digit

print("Sum of first and last digit:", sum_digits)
