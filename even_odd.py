numbers = [5,2,7,8,10,3]
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f"Even = {even}")
print(f"Odd = {odd}")