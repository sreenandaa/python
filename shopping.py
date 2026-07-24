cart = []

print("Enter the name of elements : ")

while True:
    item = input()

    if item == "done":
        break
    
    cart.append(item)

print(cart)
