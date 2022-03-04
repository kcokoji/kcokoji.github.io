import items_price
print("List of Available Products")
print("bread, beans, banana, butter, milk, coconut, chocolate, tomatoes, cocobutter, salt")
item=input("Enter the item you wish to buy: ")
qty=input("Enter the quantity: ")

if item == "milk":
    price=items_price.milk
    print("The price of ",item," is: ",items_price.milk)
    total=int(qty)*price
    print("Total is: ",total)
if item == "bread":
    price=items_price.bread
    print("The price of ",item," is: ",items_price.bread)
    total=int(qty)*price
    print("Total is: ",total)
if item == "beans":
    price=items_price.beans
    print("The price of ",item," is: ",items_price.beans)
    total=int(qty)*price
    print("Total is: ",total)
if item == "banana":
    price=items_price.banana
    print("The price of ",item," is: ",items_price.banana)
    total=int(qty)*price
    print("Total is: ",total)
if item == "butter":
    price=items_price.butter
    print("The price of ",item," is: ",items_price.butter)
    total=int(qty)*price
    print("Total is: ",total)
if item == "coconut":
    price=items_price.coconut
    print("The price of ",item," is: ",items_price.coconut)
    total=int(qty)*price
    print("Total is: ",total)
if item == "cocobutter":
    price=items_price.cocobutter
    print("The price of ",item," is: ",items_price.cocobutter)
    total=int(qty)*price
    print("Total is: ",total)
if item == "chocolate":
    price=items_price.chocolate
    print("The price of ",item," is: ",items_price.chocolate)
    total=int(qty)*price
    print("Total is: ",total)
if item == "tomatoes":
    price=items_price.tomatoes
    print("The price of ",item," is: ",items_price.tomatoes)
    total=int(qty)*price
    print("Total is: ",total)
if item == "salt":
    price=items_price.salt
    print("The price of ",item," is: ",items_price.salt)
    total=int(qty)*price
    print("Total is: ",total)