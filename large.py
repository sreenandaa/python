# sorting a set will return a list
# If I want the second-largest number, I don't need to sort everything
numbers = [8, 2, 4, 9, 6, 10]
large = numbers[0]
second = float("-inf")

# I am not using any values from the list because the list might be empty
#if I don't initialize them first, I can't use them in comparison

for num in numbers:
    if num > large:
        second = large
        large = num
#if the number is less than large, but still there is a chance the number might be greater than the present large
    elif large > num > second :
    elif large > num > second :
        second = num

print(f"Largest number = {large}")
print(f"Second largest number = {second}")
