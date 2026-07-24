# sorting a set will return a list
#if I want the sec largest number, I don't need to sort everything
numbers = [8, 2, 4, 9, 6, 10]
large = numbers[0]

for num in numbers:
    if num> large:
        large = num

print(f"Largest number = {large}")