print("Let's Explore......Shop With us....")
print("\n")
print("Choose  your Favourite products from the list..Exciting offers are Waiting..")
print("_____________________________________________________________________________")


print("**Flat  $10 discount  If cart total exceeds $200\n")

print("**Flat 5% discount on that items total price If the quantity of any single product exceeds 10 units\n")

print("**Flat  10% discount  If  total quantity exceeds 20 units\n")

print("**Flat  50% discount   ***NB: If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.\n")


print("\n")

print("Product          price")
print("______________________")
print("Product A         $20")
print("Product B         $40")
print("Product C         $50")

print("\n")

cart={}
priceperpdt=[]
quantity=[]

p1 = input("Do you Want product A ")
if p1 == "yes":
    p1='ProductA'
    P1Quantity = int(input("Enter the quantity    "))
    cart["ProductA"]=P1Quantity
    p1price=20*P1Quantity
    priceperpdt.append(p1price)
    quantity.append(P1Quantity)


p2 = input("Do you Want product B ")
if p2 == "yes":
    p2='ProductB'
    P2Quantity = int(input("Enter the quantity    "))
    cart["ProductB"]=P2Quantity
    p2price=40*P2Quantity
    priceperpdt.append(p2price)
    quantity.append(P2Quantity)


p3 = input("Do you Want product C ")
if p3 == "yes":
    p3='ProductC'
    P3Quantity = int(input("Enter the quantity    "))
    cart["ProductC"]=P3Quantity
    p3price=50*P3Quantity

    priceperpdt.append(p3price)
    quantity.append(P3Quantity)

print("\n")


print("Your items are added to cart!!!\n")
gift = input("Do you want this product is wrapped as a gift?? NB:Extra charges are included ")


prices={"productA":20,"productB":40,"productC":50}


print("your cart items are:",cart)


totalquantity=sum(cart.values())
print("Total product count=",totalquantity)

subtotal=sum(priceperpdt)



discountapplied=[]




if subtotal>200:
    discountapplied.append(("flat_10_discount", 10))
if totalquantity>20:
    discountapplied.append(("bulk_10_discount", subtotal * 0.10))

max_prdtkey = max(cart, key=cart.get)

# print(max_prdtkey)
# print(cart[max_prdtkey])

# print(priceperpdt)

if cart[max_prdtkey]>10:
    if max_prdtkey=='ProductA':
        # print('p1price=',p1price)
        discountapplied.append(("bulk_5_discount", p1price * 0.05))
    if max_prdtkey=='ProductB':
        # print('p2price=',p2price)
        discountapplied.append(("bulk_5_discount", p2price * 0.05))
    if max_prdtkey=='ProductC':
        # print('p3price=',p3price)
        discountapplied.append(("bulk_5_discount", p3price * 0.05))
            
    
if totalquantity>30:
    max_quantity = max(cart.values())
    # print(max_quantity)
    max_prdtkey = max(cart, key=cart.get)
    # print(max_prdtkey)
  
    

    if (max_quantity)>15:

        if max_prdtkey == 'ProductA':
            discount = (max_quantity-15)*(20*.50)
    if max_prdtkey == 'ProductB':
        discount = (max_quantity-15)*(40*.50)
    if max_prdtkey == 'ProductC':
        discount = (max_quantity-15)*(50*.50)

    discountapplied.append(("bulk_5_discount", discount))


print("Discount details",discountapplied)

max_discountvalue = max(discountapplied, key=lambda x: x[1])

print(' Best offer selected for uou =',max_discountvalue[0])
print('Discount amount',max_discountvalue[1])

discountamount=max_discountvalue[1]




if gift == 'yes':
    wrappinfee = totalquantity*1
    print('Gift wrap fee',totalquantity*1)
   
else:
    wrappinfee=0


shippingfee = (totalquantity//10)*5




print('Total shipping fee',shippingfee)

totalamount = ((subtotal+shippingfee+wrappinfee)-discountamount)


print("The amount you have to paid ", totalamount  )



        
        

            



      
      














