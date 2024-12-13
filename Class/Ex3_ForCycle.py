# 1st EXAMPLE: Counting loop (range of values)
print("1st EXAMPLE: Counting loop (range of values)")

sumFor = 0
for i in range(1, 6):
    sumFor += i
print(f"Sum: {sumFor}")
print(f"Last value of i: {i}")

# 2nd EXAMPLE: Iterating over the elements of a data structure (string)
print("2nd EXAMPLE: Iterating over the elements of a data structure (string)")
name = 'ALBERTO'

for letter in name:
    print(letter)
print('-----------')

for i, letter in enumerate(name):
    print(f"{i} -> {letter}")
print('-----------')

for letter in reversed(name):
    print(letter)

# 4th EXAMPLE: Dictionaries
print("4th EXAMPLE: Dictionaries")
ages = {'alberto': 23, 'ana': 55, 'armando': 19, 'arnaldo': 47}

for name in ages:  # the keys are the names
    print(name)

for name in ages.keys():  # the keys are the names
    print(name)

for age in ages.values():
    print(age)

for name, age in ages.items():
    print(name, age)
