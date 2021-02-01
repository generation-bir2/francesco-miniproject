import sys
import functions # when calling a function this way, you need to write functions.functionclear()
from functions import function_clear, print_courier_menu, print_mainmenu, print_order_menu, print_product_menu
function_clear() # clears terminal above

from core import save_products, save_couriers, save_orders

# lists
products = []
couriers = []
orders = []


# opens products file and appends stored product names to empty product list above.
with open("data/products.txt", "r") as products_file:
    for product in products_file.readlines():
        products.append(product.strip())


# opens couriers file and appends stored courier names to empty courier list above.
with open("data/data/couriers.txt", "r") as couriers_file:
    for courier in couriers_file.readlines():
        couriers.append(courier.strip())


# opens orders file and appends stored order names to empty order list above.
with open("data/orders.txt", "r") as orders_file:
    for order in orders_file.readlines():
        orders.append(order.strip())


while True:
    print_mainmenu() # main menu
    user_value = int(input("Hi, please select an option: "))
    function_clear()
    if user_value == 0:
        file = open("data/thankyou.txt", "r")
        thankyou = file.read()
        print(thankyou)
        file.close()
        sys.exit(0) # add a save function?


    elif user_value == 1: # product menu
        product_menu = True
        while product_menu == True:
            print_product_menu() # imported function
            product_input = int(input("Hi, please select a product option: "))
            function_clear()
            if product_input == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                save_products("data/products.txt", products) 
                sys.exit(0)
            elif product_input == 1:
                print("\nProducts:\n")
                print(products)
                print("\n")
            elif product_input == 2:
                functions.add_product(products) # calling a function from another file.py
            elif product_input == 3:
                functions.update_product(products)
            elif product_input == 4:
                functions.delete_product(products)
            elif product_input == 5:
                save_products("data/products.txt", products)
                product_menu = False # exits the products menu and returns the user to the main menu
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")


    elif user_value == 2: # courier menu
        courier_menu = True
        while courier_menu == True:
            print_courier_menu() # imported function
            courier_input = int(input("Hi. Please select a courier option: "))
            function_clear()
            if courier_input == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                save_couriers("data/couriers.txt", couriers)
                sys.exit(0)
            elif courier_input == 1:
                print("\nCouriers:\n")
                print(couriers)
                print("\n")
            elif courier_input == 2:
                functions.add_courier(couriers)
            elif courier_input == 3:
                functions.update_courier(couriers)
            elif courier_input == 4:
                functions.delete_courier(couriers)
            elif courier_input == 5:
                save_couriers("data/couriers.txt", couriers)
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")


    elif user_value == 3: # order menu
        order_menu = True
        while order_menu == True:
            print_order_menu() # imported function
            order_value = int(input("Hi. Please select a order option: "))
            function_clear()
            if order_value == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                save_orders("data/1orders", orders)
                sys.exit(0)
            elif order_value == 1:
                print("\nOrders:\n")
                print(orders)
                print("\n")
            elif order_value == 2:
                functions.create_new_order(orders, couriers)
            elif order_value == 3:
                pass
            elif order_value == 4:
                pass
            elif order_value == 5:
                save_orders("data/1orders", orders)
                order_menu = False
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")