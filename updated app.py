import core

core.mainmenu_func()

# function_clear()

# while True:
#     option = int(input(core.welcome))
#     if option == 0: # opens the file, writes file, then 'breaks'
#         file = open("products.txt", "w")
#         for item in core.available_products:
#             file.write(f"{item}\n")
#         file.close()
#         break
#     if option == 1:
#         while True:
#             alternative_option_1 = int(input(core.mainmenu))
#             if alternative_option_1 == 0:
#                 break
#             if alternative_option_1 == 1:

#                 for drinks in core.available_products: # for loop, prints every drink vertically
#                     print(drinks)
#                 print('\n')
#                 input("Press enter to continue")
            
#             if alternative_option_1 == 2:
#                 products_contents = input("What product would you like?: \n") # if they type 'water', now water is product content, duh
#                 core.available_products.append(core.products_contents)
#                 print('\n')
#                 for drinks in core.available_products: # for loop, prints every drink vertically
#                     print(drinks)
#                 print('\n')
#                 input("Press enter to continue")
            
#             if alternative_option_1 == 3: # this is a code that occurs when a user wants to update a product
#                 heres_the_product = 0 # to do with the scope of local variable
#                 update_product = input(f"These are the available products: {core.available_products} \n")
#                 for index in range(len(core.available_products)): # replace product one way is use for loop.
#                     if core.available_products[index] == update_product: # if their input exists in available product and only in that circumstance, the next 3 lines will be run
#                         heres_the_product = index # heres the product is the location(index) of the item the user wants to replace
#                         new_drink = input("What drink would you want?: \n" ) # INPUT THAT'S A VARIABLE NOW
#                         core.available_products[heres_the_product] = new_drink # heres_the_product replaces the exact index within the list
#                         # print(heres_the_product) not needed

#                 for drinks in core.available_products: # for loop, prints every drink vertically
#                     print(drinks)
#                 print('\n')
#                 input("Press enter to continue")
                
#             if alternative_option_1 == 4:
#                 delete_product = input("What drink don't you like?: \n") #input, I'm asking the user
#                 try:
#                     core.available_products.remove(delete_product)
                    
#                 except ValueError:
#                     print("ERROR 404. Product unavailable. Brexit happened.")                   
#     if option == 2: 
#         while True:
#             alternative_option_2  = int(input(core.couriers_menu)) 
#             if alternative_option_2 == 0:
#                 file = open("couriers.txt", "w")
#                 for item in core.available_products:
#                     file.write(f"{item}\n")
#                 file.close()
#                 break
#             if alternative_option_2 == 1:
#                 print(core.couriers.read())
#             if alternative_option_2 == 2:
#                 new_courier = input("What is the name of courier: \n")
#                 core.couriers.append(new_courier)