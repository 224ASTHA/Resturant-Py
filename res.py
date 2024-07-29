
menu_food = {
            "Pizza":150,
            "Pasta":90, 
            "Burger":80,
            "French Fries":100,
            "Shawarma":70
    }

menu_drinks = {
    "Coca-Cola":50,
    "Sprite":60,
    "Mojito":100,
    "Cold-Coffee":20
}

total_order1 = 0
total_order2 = 0
final_bill = 0


def orderMade_food ():
    item = input("Enter the name of the item you want to order = ")
    global total_order1
    if item in menu_food:
        total_order1 = total_order1 + menu_food[item]
    
    print(f"Your item {item} has been added to your order")
    return total_order1

def orderMade_drinks ():
    item1 = input("Enter the name of the item you want to order = ")
    global total_order2
    if item1 in menu_drinks:
        total_order2 = total_order2 + menu_drinks[item1]
    
    print(f"Your item {item1} has been added to your order")
    return total_order2

def res ():
    print("Welcome to our Restarurant . Here's the menu: ")
    print("Pizza : Rs 150 \n Pasta : Rs 90 \n Burger : Rs 80 \n French Fries : Rs 100 \n Shawarma : Rs 70")
    print("Some Drinks for you!")
    print("Coca-Cola : Rs 50 \n Sprite : Rs 60 \n Mojito : Rs 100 \n Cold-Coffee : Rs 20")

    ans = input("Do you want to order (yes/no)")
    i = 0

    while(ans == "yes"):
      food_price = orderMade_food()
      ans = input("Do you want to order (yes/no)")
    
    print(f"Your total price for food is : {food_price}")

    ans1 = input("Anything for the drinks (yes/no)")

    while(ans1 == "yes"):
      drink_price = orderMade_drinks()
      ans1 = input("Do you want to order (yes/no)")
    
    print(f"Your total price for drinks is : {drink_price}")

    global final_bill
    final_bill = food_price + drink_price
    print(f"Thank you for visting your total bill is : {final_bill}")

res()