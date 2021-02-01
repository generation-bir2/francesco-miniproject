import sys
import functions # when calling a function this way, you need to write functions.function_clear() functions is your functions.py file
import core

# lists
products = []
couriers = []
orders = []


# opens products file and appends stored product names to empty product list above.
with open("data/products.txt", "r") as products_file:
    for product in products_file.readlines():
        products.append(product.strip())


# opens couriers file and appends stored courier names to empty courier list above.
with open("data/couriers.txt", "r") as couriers_file:
    for courier in couriers_file.readlines():
        couriers.append(courier.strip())


# opens orders file and appends stored order names to empty order list above.
with open("data/orders.txt", "r") as orders_file:
    for order in orders_file.readlines():
        orders.append(order.strip())


while True:
    functions.function_clear()
    functions.print_mainmenu() # main menu
    user_value = int(input("Hi, please select an option: "))
    functions.function_clear()
    if user_value == 0:
        file = open("data/thankyou.txt", "r")
        thankyou = file.read()
        print(thankyou)
        file.close()
        sys.exit(0)


    elif user_value == 1: # product menu
        product_menu = True
        while product_menu == True:
            functions.print_product_menu() # imported function
            product_input = int(input("Hi, please select a product option: "))
            functions.function_clear()
            if product_input == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                core.save_products("data/products.txt", products) # imported function from core
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
                core.save_products("data/products.txt", products)
                product_menu = False # exits the products menu and returns the user to the main menu
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")


    elif user_value == 2: # courier menu
        courier_menu = True
        while courier_menu == True:
            functions.print_courier_menu() # imported function
            courier_input = int(input("Hi. Please select a courier option: "))
            functions.function_clear()
            if courier_input == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                core.save_couriers("data/couriers.txt", couriers)
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
                core.save_couriers("data/couriers.txt", couriers)
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")


    elif user_value == 3: # order menu
        order_menu = True
        while order_menu == True:
            functions.print_order_menu() # imported function
            order_value = int(input("Hi. Please select an order option: "))
            functions.function_clear()
            if order_value == 0:
                file = open("data/thankyou.txt", "r")
                thankyou = file.read()
                print(thankyou)
                file.close()
                core.save_orders("data/orders.txt", orders)
                sys.exit(0)
            elif order_value == 1:
                print("\nOrders:\n")
                print(orders)
                print("\n")
            elif order_value == 2:
                functions.order_add(orders, couriers)
            elif order_value == 3:
                functions.order_update(orders)
            elif order_value == 4:
                pass
            elif order_value == 5:
                core.save_orders("data/orders.txt", orders)
                order_menu = False
            else:
                print("\nI am sorry. This is not an option. Please select another choice.\n")