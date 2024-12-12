
total_sales = 0.0

product_names = []
product_prices = []
product_quantities= []


def show_menu():
    print("\n---DRUGSTORE MANAGEMENT MENU---")
    print("1. Sell ​​Product")
    print("2. Show Inventory")
    print("3. Show Total Sales")
    print("4. Close")
    
def sell_product():
    print("\nSell Product")
    product_name_sell = enter_product_name()
    product_quantity_sell = enter_product_quantity(product_name_sell)
    
    exist_product = False
    
    for i in range(len(product_names)):
        global total_sales
        if product_names[i] == product_name_sell:
            exist_product = True
            if product_quantities[i] > product_quantity_sell:
                total_sell = product_quantity_sell * product_prices[i]
                total_sales += total_sell
                product_quantities[i] -= product_quantity_sell
                print(f"Sale made. The total of this sale was ${total_sell:.2f}")
                print(f"There are {product_quantities[i]} units of {product_name[i].capitalize()} left in inventory.")
            else:
                print(f"Insufficient quantity in inventory, only {product_quantities[i]} units left in stock.")
                break
        else: 
            continue
    if not exist_product:
        print("Product not found in inventory")

def show_product_inventory():
    print("\nShow Inventory")
    for i in range(len(product_names)):
        print(f"Producto { i + 1 }: { product_names[i].capitalize() }, price: {product_prices[i]:.2f}, Quantity: {product_quantities[i]}")
     
def enter_product_quantity(product_name):
    return int(input(f"Enter the amount of { product_name.capitalize() }: "))

def enter_product_name():
    return input(f"Enter the name of the product: ").lower()


product_num = int(input("Enter the number of products to manage: "))

for i in range(product_num):
    print(f"Product { i + 1 }")
    product_name = input("Enter the name of the product: ").lower()
    product_price = float(input(f"Enter the price of { product_name.capitalize() }: "))
    product_quantity = int(input(f"Enter the amount of { product_name.capitalize() }: "))
    
    product_names.append(product_name)
    product_prices.append(product_price)
    product_quantities.append(product_quantity)
    


while True:
    show_menu()
    selected_option = int(input("Select An Option: "))
    
    if selected_option == 1:
        sell_product()
    elif selected_option == 2:
        show_product_inventory()
    elif selected_option == 3:
        print("\nShow Total Sales")
        print(f"Total accumulated sales is {total_sales}")
    elif selected_option == 4:
        break
    else:
        print("Incorrect option. You must select one of the options from the menu.")        
        
