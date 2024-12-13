# 1st Example: Counting loop (range of values)
print("Counting loop (range of values)")

# Sum(Range 5)
i = 1
sumWhile = 0

while i <= 5:
    sumWhile += i
    i += 1
print(f"The sum total is: {sumWhile}")
print(f"Last value of i: {i}")

# 2nd Example: Iterating over the elements of a data structure (string)
print("Iterating over the elements of a data structure (string)")

i = 0
name = 'Alberto'

while i < len(name):
    print(name[i])
    i += 1
print('------------')

i = 0
while i < len(name):
    print(f"{i} -> {name[i]}")
    i += 1
print('-----------')

i = len(name) - 1
while i > -1:
    print(name[i])
    i -= 1

# 3rd Example: Iterating over the elements of a data structure (list)
print('Iterating over the elements of a data structure (list)')
values = [10, -50, 40, .29]

i = 0
sumList = 0

while i < len(values):
    sumList += values[i]
    i += 1
print(f"The sum of the list is: {sumList}")

# 4th Example: Validation Cycle
print('Validation Cycle')
age_str = input("Age? ")

while not age_str.isdigit():
    print("Invalid age")
    age_str = input("Age? ")
print(f"The double is: {2 * int(age_str)}")
print('------')

while True:
    age_str = input("Age? ")
    if age_str.isdigit():
        break
    print("Invalid age")
print(f"The double is {2 * int(age_str)}")

# 5th EXAMPLE: Menu of options
print("5th EXAMPLE: Menu of options")

option = ''
while option != 'T':
    # 1. Display the menu of options
    print("1 - WITHDRAW")
    print("2 - DEPOSIT")
    print("3 - CHECK BALANCE")
    print("T - TERMINATE")
    print()

    # 2. Ask the user for an option
    option = input("Option: ")

    # 3. Analyze and execute the entered option
    match option:
        case '1':
            print("Option WITHDRAW chosen")
        case '2':
            print("Option DEPOSIT chosen")
        case '3':
            print("Option CHECK BALANCE chosen")
        case 'T':
            print("End of the program")
        case _:
            print(f"Invalid option {option}")

    # 3. Analyze and execute the entered option (with IF)
    # if option == '1':
    #     print("Option WITHDRAW chosen")
    # elif option == '2':
    #     print("Option DEPOSIT chosen")
    # elif option == '3':
    #     print("Option CHECK BALANCE chosen")
    # elif option == 'T':
    #     print("End of the program")
    # else:
    #     print(f"Invalid option {option}")

    # 3. Analyze and execute the entered option (with DICTIONARIES)
    # def withdraw():
    #     print("Option WITHDRAW chosen")

    # def deposit():
    #     print("Option DEPOSIT chosen")

    # def default():
    #     print(f"Invalid option {option}")

    # action = {
    #     '1': withdraw,
    #     '2': deposit,
    # }.get(option, default)

    # action()

    print()
