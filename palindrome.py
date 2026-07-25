origin = "malayalam"
print(f"origin = {origin}")
reverse = "".join(reversed(origin))
print(f"reverse = {reverse}")
flag = 0
for i in range(len(origin)):
    if origin[i] != reverse[i]:
        flag = 1
        break

if flag == 0:
    print("It is palindrome")
else:
    print("It is not a palindrome")
        
