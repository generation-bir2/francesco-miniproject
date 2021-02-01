import os

def function_clear():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    
def print_mainmenu():
    file = open("data/mainmenu.txt", "r")
    mainmenu = file.read()
    print(mainmenu)
    file.close()
    
def print_product_menu():
    file = open("data/productmenu.txt", "r")
    productmenu = file.read()
    print(productmenu)
    file.close()

def add_product(product_list):
    new_product = input(
'''
Press 0 to go back.

What product would you like to add?

''')
    if new_product.strip() == "0":
        return
    else:
        product_list.append(new_product.title().strip())
        print("\nProducts:\n")
        print(product_list)
        print("\n")

def update_product(product_list):
    product = input(
'''
Press 0 to go back.

What product would you like to update?

''')
    if product.title().strip() in product_list:
        updated_product = input("What would you like to update it to? ")
        product_index = product_list.index(product.title().strip())
        product_list[product_index] = updated_product.title().strip()
        print("\nProducts:\n")
        print(product_list)
        print("\n")
        return product_list
    elif product.strip() == "0":
        return
    else:
        print("\nWe apologise for this incovenience. We do not have this product in stock.\n")

def delete_product(product_list):
        product = input(
'''
Press 0 to go back.

What product would you like to delete?

''')
        if product.title().strip() in product_list:
            product_index = product_list.index(product.title().strip())
            product_list.pop(product_index)
            print("\nProducts:\n")
            print(product_list)
            print("\n")
            return product_list
        elif product.strip() == "0":
            return
        else:
            print("\nWe apologise for this incovenience. We do not have this product in stock.\n")

def print_courier_menu():
    file = open("data/couriermenu.txt", "r")
    couriermenu = file.read()
    print(couriermenu)
    file.close()

def add_courier(courier_list):
    new_courier = input(
'''
Press 0 to go back.

Which courier would you like to add?

''')
    if new_courier.strip() == "0":
        return
    else:
        courier_list.append(new_courier.title().strip())
        print("\nCouriers:\n")
        print(courier_list)
        print("\n")
        return courier_list
    
def update_courier(courier_list):
    courier = input(
'''
Press 0 to go back.

Which courier would you like to update?

''')

    if courier.title().strip() in courier_list:
        courier_index = courier_list.index(courier.title().strip())
        courier_list.pop(courier_index)
        print("\nCouriers:\n")
        print(courier_list)
        print("\n")
        return courier_list
    elif courier.strip() == "0":
        return
    else:
        print("\nWe apologise for this incovenience. We do not have this courier in our database.\n")

def delete_courier(courier_list):
    courier = input(
'''
Press 0 to go back.

Which courier would you like to delete?

''')
    if courier.title().strip() in courier_list:
        courier_index = courier_list.index(courier.title().strip())
        courier_list.pop(courier_index)
        print("\nCouriers:\n")
        print(courier_list)
        print("\n")
        return courier_list
    elif courier.strip() == "0":
        return
    else:
        print("\nWe apologise for this incovenience. We do not have this courier in our database.\n")

def print_order_menu():
    file = open("data/ordermenu.txt", "r")
    order_menu = file.read()
    print(order_menu)
    file.close()

def order_add(order_list, courier_list): # update it for other functions too
    new_order = {}
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone = input("What is your mobile phone? ")
    status = "Preparing"
    print("\nCouriers:\n")
    print(courier_list)
    print("\n")
    courier = input("Which courier would you like? ") # ASK THE USER TO SELECT A COURIER FROM THE LIST
    if courier.title().strip() in courier_list: 
        new_order["Name"] = name.title().strip()
        new_order["Address"] = address.title().strip()
        new_order["Phone Number"] = phone.strip()
        new_order["Status"] = status # SET THE DEFAULT ORDER STATUS TO BE PREPARING
        order_list.append(new_order) # APPEND THE NEW ORDER TO THE LIST OF ORDERS
        return order_list
    else:
        print("\nWe apologise for this incovenience. We do not have this courier in our database.\n")


def order_update(order_list):
    print_order_menu()
    idx = int(input("Select: "))
    for key in order_list[idx].keys():
        update = input(f"{key}: ")
        if update != "":
            if key == "customer_phone" or key == "courier":
                order_list[idx][key] = int(update)
            else:
                order_list[idx][key] = update
    print_order_menu()
    return order_list