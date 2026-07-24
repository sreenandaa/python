# sorting a set will return a list
#if I want the sec largest number, I don't need to sort everything
numbers = [8, 2, 4, 9, 6, 10]
large = numbers[0]
second = float("-inf")
for num in numbers:
    if num > large:
        second = large
        large = num
    elif large > num > second :
        second = num

print(f"Largest number = {large}")
print(f"Second largest number = {second}")