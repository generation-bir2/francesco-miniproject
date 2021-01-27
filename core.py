import os

#function to clear terminal
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def function_clear():
    clear()

list_products = []

# this reads the content of welcome/main menu txt file; saves to "mainmenu"
file = open("mainmenu.txt", "r")
mainmenu = file.read()
file.close()

# this reads the content of products.txt file; saves to available_products
def read_products():
    file = open("products.txt", "r")
    available_products = file.readlines() # return all lines in the file, as a list where each line is an item in the list object.
    file.close()
    for line in range(len(available_products)):
        available_products[line] = available_products[line].strip() # remove spaces at the beginning and at the end of the string - line is an index
        # available_products is of the type list of strings
        
    return available_products # this is going to returning the avalable products

# this reads the content of couriers.txt file; saves to couriers
def read_couriers():
    file = open("couriers.txt", "r")
    available_couriers = file.readlines()
    file.close()
    for line in range(len(available_couriers)):
        available_couriers[line] = available_couriers[line].strip()
        # available_couriers is of the type list of strings
        
    return available_couriers

def exit_func(list_products, list_couriers): # list_products, list_couriers representative of available_products and couriers
    file = open("products.txt", "w") # save/write products to file
    for products in list_products: # file.writelines(available_products) NO NEED for this now because of for loop
        file.write(f"{products}\n")
    file.close()

    file = open("couriers.txt", "w") #save couriers to file ("w")
    for couriers in list_couriers:
        file.write(f"{couriers}\n")
    file.close()
    exit() #exit

def read_products():
    
    products = []
    
    try: # File Context Manager. pg 25
        with open('products.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip() # stripping the \n, tabs, spaces
                products.append(line)

    except:
        print('ERROR 404. Products unavailable.')
        
    return products

def productsmenu_func(products_list):
    function_clear() # it clears the whatever that was in the terminal (main menu)
    print_product_menu()
    user_option = int(input("Select an option\n"))
    if user_option == 0:
        return
    
    elif user_option == 1:
        print(products_list)
        input("Press enter to continue.")
        
    elif user_option == 2:
        adding_product = input("What product would you like to add?: ")
        createToList(aList = products_list, entry = adding_product) # we're (calling) creating a new product in product_list via aList (aList= not really needed)
    
    elif user_option == 3:
        print(products_list) 
        new_product_update = input("What product would you like to update?: ") # updateList will be the item that the user wants to change
        updateList(aList = products_list, entry = new_product_update) # we're (calling) updating a new product in product_list
    productsmenu_func(list_products) # goes back to the product menu 
    
def print_product_menu():
    print('''

Hi. Please choose an option:

[0] : Return
[1] : View all products
[2] : Create a new product
[3] : Update product
[4] : Delete product
'''
)

def couriersmenu_func(couriers_list):
    # reads and saves Couriers Menu to couriersmenu
    file = open("couriersmenu.txt", "r")
    couriersmenu = file.read()
    file.close()
    
    user_option = int(input(couriersmenu))
    if user_option == 0:
        return couriers_list
    elif user_option == 2:
        view_list(couriers_list) # view_list is a def func
        input("Press Enter")
        
    #lets users view, add, update or remove from couriers

def view_list(aList):
    print()
    # for each in aList
        # print (each)
    # wait for user input to dissapear
    # return None (basically going back to the previous menu)
    pass

def createToList(aList, entry):
    aList.append(entry) # append to aList entry
                        # return the aList
    
def updateList(aList:list, entry:str):
    product_exists = False # We assume the users choice doesnt exist
    for index in range(len(aList)): # aList:list == products_list 
        if entry == aList[index] : # checking if an item in our list is the same as what the user entered 
            product_exists = True #if the product exists -> ask the user what they want to change it to
            new_product = input("What product would you like to update to?: ") 
            aList[index] = new_product
    if product_exists == False:  # if the product doesn't exist - tell the user it doesn't exist
        print("ERROR 404.")
    
    input("Press enter to continue" )
    productsmenu_func(aList)  # return to the product menu

def removeFromList(aList, index):
    #aList.pop(index)
    #return aList
    pass

def mainmenu_func(list_products, list_couriers):
    function_clear()
    option = int(input(mainmenu))
    if option == 0:
        exit_func(list_products, list_couriers)
    elif option == 1:
        productsmenu_func(list_products)
    elif option == 2:
        couriersmenu_func(list_couriers) # TypeError: couriersmenu_func() missing 1 required positional argument: 'couriers_list'
    else: 
        input("Please input a valid option\nPress Enter")
        mainmenu_func(list_products, list_couriers)
    #code ends if it reaches here (Which is does)

if __name__ == "__main__": # when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
    list_products = read_products()
    list_couriers = read_couriers()
    mainmenu_func(list_products, list_couriers)