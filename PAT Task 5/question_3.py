numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenSquares = [x**2 for x in numbers if (lambda n: n % 2 == 0)(x)]

print(evenSquares)
