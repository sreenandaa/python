fruit = "banana"
frequency = {}
for char in fruit:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

print(frequency)