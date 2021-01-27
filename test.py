import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # each time you draw a new menu, add clear()
def function_clear():
    clear()
    
function_clear()

file = open("mainmenu.txt", "r") # if I were to use print(), it is going to get printed twice
welcome = file.read()
file.close()

file = open("products.txt", "r")
available_products = file.readlines() # return all lines in the file, as a list where each line is an item in the list object.
file.close()

for line in range(len(available_products)):
    available_products[line] = available_products[line].strip() # remove spaces at the beginning and at the end of the string - line is an index

file = open("couriers.txt", "r")
couriers = file.read()
file.close()


file = open("productsmenu.txt", "r")
productmenu = file.read()
file.close()

couriers_menu = '''

Please choose an option:

[0] Return
[1] View all couriers
[2] Create a new courier
[3] Update courier
[4] Delete courier

'''


while True:
    option = int(input(welcome))
    if option == 0: # opens the file, writes file, then 'breaks'
        file = open("products.txt", "w")
        for item in available_products:
            file.write(f"{item}\n")
        file.close()
        break
    if option == 1:
        while True:
            alternative_option_1 = int(input(productmenu))
            if alternative_option_1 == 0:
                break
            if alternative_option_1 == 1:

                for drinks in available_products: # for loop, prints every drink vertically
                    print(drinks)
                print('\n')
                input("Press enter to continue")
            
            if alternative_option_1 == 2:
                products_contents = input("What product would you like?: \n") # if they type 'water', now water is product content, duh
                available_products.append(products_contents)
                print('\n')
                for drinks in available_products: # for loop, prints every drink vertically
                    print(drinks)
                print('\n')
                input("Press enter to continue")
            
            if alternative_option_1 == 3: # this is a code that occurs when a user wants to update a product
                heres_the_product = 0 # to do with the scope of local variable
                update_product = input(f"These are the available products: {available_products} \n")
                for index in range(len(available_products)): # replace product one way is use for loop.
                    if available_products[index] == update_product: # if their input exists in available product and only in that circumstance, the next 3 lines will be run
                        heres_the_product = index # heres the product is the location(index) of the item the user wants to replace
                        new_drink = input("What drink would you want?: \n" ) # INPUT THAT'S A VARIABLE NOW
                        available_products[heres_the_product] = new_drink # heres_the_product replaces the exact index within the list
                        # print(heres_the_product) not needed

                for drinks in available_products: # for loop, prints every drink vertically
                    print(drinks)
                print('\n')
                input("Press enter to continue")
                
            if alternative_option_1 == 4:
                delete_product = input("What drink don't you like?: \n") #input, I'm asking the user
                try:
                    available_products.remove(delete_product)
                    
                except ValueError:
                    print("ERROR 404. Product unavailable. Brexit happened.")
                    


    if option == 2: 
        while True:
            alternative_option_2  = int(input(couriers_menu)) 
            if alternative_option_2 == 0:
                file = open("couriers.txt", "w")
                for item in available_products:
                    file.write(f"{item}\n")
                file.close()
                break
            if alternative_option_2 == 1:
                print(couriers.read())
            if alternative_option_2 == 2:
                new_courier = input("What is the name of courier: \n")
                couriers.append(new_courier)