products={}
while True:
    product_name=input("enter the product name:")
    if product_name.lower()=='done':
        break
    price=float(input(f"enter price for {product_name}:"))
    products[product_name]=price
while True:
    product_name=input("enter the product name for the product price:")
    if product_name.lower()=='exit':
        break
    if product_name in products:
        print(f"price of the{product_name} is {products[product_name]}")
    else:
        print(f"sorry,{product_name} is not in list")

    

