num1 = [1,2,3,4,5]
num2 = []

for i in range(len(num1)-1,-1,-1):
    num2.append(num1[i])
    
print(num2)