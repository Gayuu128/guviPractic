people = [
    {"name": "Gautham", "age": 17},
    {"name": "Gayuu", "age": 22},
    {"name": "Mithun", "age": 16},
    {"name": "Divya", "age": 19},
    {"name": "Tham", "age": 30}
]
# Filter people who are 18 or older
adults = filter(lambda person: person["age"] >= 18, people)

# Map their names to a new list
adult_names = list(map(lambda person: person["name"], adults))

print(adult_names)
