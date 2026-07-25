numbers = [2, 3, 5, 7, 9]

i = 1
j=0
while j < len(numbers):
    if i != numbers[j]:
        print(f"{i} is missing")
        i += 1
        continue
    i += 1
    j += 1
   