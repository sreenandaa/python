old_list = [1,2,2,3,4,4,5]
new_list = []
seen = set()

for number in old_list:
    if number not in seen:
        seen.add(number)
        new_list.append(number)

print(new_list)
