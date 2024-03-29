import read
import write

#Checks validity of ID
def valid_id_for_purchase(value):
   
    valid_id = False
    while not valid_id:
        try:
            ID = int(input("Enter the ID of the Laptop to purchase: "))
            if ID > 0 and ID <= len(value):
                valid_id = True
                return ID
            else:
                read.invalid_input()
        except ValueError:
            read.invalid_input()

#Checks validity of quantity
def valid_quantity_for_purchase(value):
    
    quantity_validity = False
    while not quantity_validity:
        try:
            quantity = int(input("How many laptops do you want to purchase? "))
            if quantity > 0:
                quantity_validity = True
                return quantity
            else:
                read.invalid_input()
        except ValueError:
            read.invalid_input()


#Function for the purchase of the laptop
def make_purchase():
   
    contents = write.read_file()
    value = write.dictionary(contents)

    add_to_cart = []
    continue_loop = True
    while continue_loop:  # outerloop
        write.print_laptop_list(value) 
        ID = valid_id_for_purchase(value)
        quantity = int(valid_quantity_for_purchase(value))
        value[ID][3] = int(value[ID][3]) + quantity
        add_to_cart.append([ID, quantity])

        write.write_text_file(value)
        write.print_laptop_list(value)

        additional = True
        while additional == True:  # inner loop
            user_input = input("Do you want to buy more laptop?(Y/N) :")
            if user_input.upper() == "N":
                continue_loop = False  
                additional = False  

            elif user_input.upper() == "Y":
                continue_loop = True  
                additional = False  

            else:
                read.invalid_input()
                additional = True 

    print()

     # function to print and write the bill
    write.write_purchase_bill(add_to_cart) 
    read.make_purchase()


#Check the validity of ID and display required message.
def valid_id_for_sell(value):
    valid_data = False
    while valid_data == False:
        try:
            ID = int(input("Enter the ID of the laptop you want to sell: "))

            # ID shouldn't be less than 0 and greater/equal to the length of the dictionary
            if 0 < ID <= len(value):  
                if int(value[ID][3]) > 0:
                    valid_data = True
                    return ID
                else:
                    read.out_of_stock()
            else:
                read.invalid_input()
        except:
            read.invalid_input()


#Checks the available quantity of the laptop
def valid_quantity_for_sell(value, ID):
    quantity_validity = False
    while quantity_validity == False:
        try:
            quantity = int(input("How many laptops do you want to sell? "))
            if quantity > 0 and quantity <= int(value[ID][3]):
                quantity_validity = True
                return quantity
            else:
                read.span()
        except:
            read.invalid_input()


#Function for the sell of laptop
def make_sell():

    contents = write.read_file()
    value = write.dictionary(contents)

    add_to_cart = []
    write.print_laptop_list(value)
    continue_loop = True  
    while continue_loop:  # outerloop

        ID = valid_id_for_sell(value)
        if int(value[ID][3]) <= 0:
            read.span()
            continue_loop = False
        else:
            read.available_laptops()
            quantity = valid_quantity_for_sell(value, ID)
            value[ID][3] = int(value[ID][3]) - quantity
            add_to_cart.append([ID, quantity])

        write.write_text_file(value)
        write.print_laptop_list(value)

        additional = True
        while additional:  # innerloop
            user_input = input("Do you want to sell more laptops?(Y/N) :")

            if user_input.upper() == "N":
                continue_loop = False  
                additional = False 

            elif user_input.upper() == "Y":
                continue_loop = True  
                additional = False  

            else:
                read.invalid_input()
                additional = True  

    print()
    # Function for printing and writing the bill
    write.write_sell_bill(add_to_cart)  
    read.make_sell()




