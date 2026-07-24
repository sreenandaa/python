numbers = [8,2,4,9,6,10,10]
new = sorted(list(set(numbers)))
print(new)
print(f"The second largest number : {new[len(new)-2]} ")
