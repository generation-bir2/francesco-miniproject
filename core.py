# saves products, couriers, orders txt files

def save_products(myfile: str, data: list):
    with open(myfile, "w") as products_file:
        for item in data:
            products_file.write(item + "\n")

def save_couriers(myfile: str, data: list): 
    with open(myfile, "w") as couriers_file:
        for item in data:
            couriers_file.write(item + "\n")
            
# def save_orders(myfile: str, data: list): 
    # for CSV 
    # with open(myfile, "w") as orders_file:
    #     for item in data:
    #     orders_file.write(item + "\n")