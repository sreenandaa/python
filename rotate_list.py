num1 = [1,2,3,4,5]
num2 = []
i = -1
while abs(i) < len(num1):
    num2.append(num1[i])
    if i == -(len(num1)):
        break
    i = i - 1
print(num2)