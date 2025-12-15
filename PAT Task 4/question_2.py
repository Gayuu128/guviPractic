numbers = [10, 501, 22, 37, 100, 999, 87, 351]

primeNum = []

for num in numbers:
    if num > 1:
        isPrime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            primeNum.append(num)

print("Prime Numbers:", primeNum)
print("Count of Prime Numbers:", len(primeNum))
