import read
import datetime


#Function to call data from the text file
def read_file():
    file = open("laptop_details.txt", "r")
    input = file.readlines()
    file.close()
    return input


# Function to convert file's content into dictionary
def dictionary(content):
    input = {}
    for index in range(len(content)):
        input[index + 1] = content[index].replace("\n", "").split(",")
    return input


#Function to read text file and display list
def print_laptop_list(value):
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("ID", "\t", "Laptop Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "GEN", "\t","\t", "CPU")
    print("-----------------------------------------------------------------------------------------------------------\n")
    for key, data in value.items():  
        print(key, "\t", data[0], "\t", data[1], "\t", data[2], "\t", data[3], "\t""\t", data[4], "\t", data[5])

    print("-----------------------------------------------------------------------------------------------------------\n")


#Function to write and manipulate the text file
def write_text_file(value):
    file = open("laptop_details.txt", "w")
    for data in value.values():
        write_data = str(data[0]) + "," + str(data[1]) + "," + str(data[2]) + "," + str(data[3]) + "," + str(
            data[4]) + "," + str(data[5]) + "\n"
        file.write(write_data)
    file.close()


#Function to update date and time in bills
def date_and_time():

    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    Hour = datetime.datetime.now().hour
    Minute = datetime.datetime.now().minute

    Date = (str(Year) + "-" + str(Month) + "-" + str(Day) + " " + str(Hour) + ":" + str(Minute))
    return Date


def getdate():

    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day

    Date = (str(Year) + "-" + str(Month) + "-" + str(Day))
    return Date


#Function to alter purchase bills
def write_purchase_bill(add_to_cart):
    
    contents = read_file()
    value = dictionary(contents)
    
    alphabetic_form = False
    while alphabetic_form == False: 
        Customer_Name = input("Please Enter the name of the customer: ")
        if Customer_Name.isalpha(): 
            alphabetic_form = True
        else:
            read.invalid()
            
    int_contact = False
    while int_contact == False:
        try:
            Contact = int(input("Please enter your contact number: "))
            int_contact = True
        except:
            read.invalid()

    #Printing Bills
    print("\n--------------------------INVOICE------------------------------")
    print("\n" + "Name: " + Customer_Name)
    print("Phone no.: " + str(Contact))
    Date = date_and_time()
    print("Purchase Date: " + str(Date))
    
    print("-----------------------------------------------------------------------------------------------------------")
    print("ID", "\t", "Customer Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "CPU", "\t\t", "Graphics")
    print("-----------------------------------------------------------------------------------\n")

    Total = 0
    for index in range(len(add_to_cart)):
        ID = int(add_to_cart[index][0])
        Quantity = int(add_to_cart[index][1])
        Name = value[ID][0]
        Brand = value[ID][1]
        Price = int(value[ID][2].replace("$", "")) * Quantity
        CPU = (value[ID][4])
        Graphics = (value[ID][5])
        Total = Price * Quantity
        Total += Total

        print(str(index + 1), "\t", Name, "\t", Brand, "\t", str(Price), "\t", str(Quantity), "\t", CPU, "\t\t", Graphics)
        print("\n")

    Total_VAT = (Total + (Total * 13/100))
    print("Total purchase = " + str(Total) + "\n")
    print("Total purchase with 13% vat = " + str(Total_VAT) + "\n")

    # bill generation(writing bill) starts here
    file = open(Customer_Name + "_" + str(getdate()) + ".txt", "w")  # a text file with the name of the user is created

    file.write("\n------------------------INVOICE------------------------\n")
    file.write("\n" + "Name: " + Customer_Name + "\n")
    file.write("Phone no.: " + str(Contact) + "\n")
    Date = date_and_time()
    file.write("Date: " + str(Date) + "\n\n")

    file.write("-----------------------------------------------------------------------------------------------------------")
    file.write("\nID  \tLaptop Name  \tBrand  \tPrice  \tQuantity  \tCPU  \tGraphics  \n")
    file.write("-----------------------------------------------------------------------------------------------------------\n\n")

    Total = 0
    for index in range(len(add_to_cart)):
        ID = int(add_to_cart[index][0])
        Quantity = int(add_to_cart[index][1])
        Name = value[ID][0]
        Brand = value[ID][1]
        Price = int(value[ID][2].replace("$", "")) * Quantity
        CPU = (value[ID][4])
        Graphics = (value[ID][5])
        Total = Price * Quantity
        Total += Total

        file.write(str(index + 1) + "\t" + Name + "\t" + Brand + "\t" + str(Price) + "\t" + str(Quantity) + "\t" + CPU + "\t" + Graphics)
        file.write("\n\n")

    Total_VAT = (Total + (Total*13/100))
    file.write("\n-----------------------------------------------------------------------------------------------------------\n\n")
    file.write("Total purchase: " + str(Total)+ "\n")
    file.write("Total purchase  with 13% vat = " + str(Total_VAT)+ "\n")
    file.write("\n-----------------------------------------------------------------------------------------------------------")
    file.write("\n       Thank you! The laptops have been PURCHASED successfully.   \n")          
    file.write("-----------------------------------------------------------------------------------------------------------\n")

    file.close()


#Function to generate bills of sold laptops
def write_sell_bill(add_to_cart):

    contents = read_file()
    value = dictionary(contents)

    alphabetic_form = False
    while alphabetic_form == False:
        Customer_Name = input("Please Enter the name of the customer: ")
        if Customer_Name.isalpha():
            alphabetic_form = True
        else:
            read.invalid_input()

    int_contact = False
    while int_contact == False:
        try:
            Contact = int(input(" Please Enter the contact number of the customer: "))  
            int_contact = True 
        except:
            read.invalid_input() 

    #Printing of bills
    print("\n--------------- INVOICE ---------------\n")
    print("\n" + "Name: " + Customer_Name)
    print("Phone no.: " + str(Contact))
    Date = date_and_time()
    print("Sold Date: " + str(Date) + "\n")

    print("\n-----------------------------------------------------------------------------------------------------------")
    print("ID", "\t", "Customer Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "CPU", "\t", "Graphics")
    print("-----------------------------------------------------------------------------------------------------------\n")

    Total = 0
    for index in range(len(add_to_cart)):
        ID = int(add_to_cart[index][0])
        Quantity = int(add_to_cart[index][1])
        Name = value[ID][0]
        Brand = value[ID][1]
        Price = int(value[ID][2].replace("$", "")) * Quantity
        CPU = (value[ID][4])
        Graphics = (value[ID][5])
        Grand_Total = Price * Quantity
        Total += Grand_Total

        print(str(index + 1), "\t", Name, "\t", Brand, "\t", str(Price), "\t", str(Quantity), "\t", CPU, "\t", Graphics)
        print("\n")

    total_price_with_shipping_cost = Total + 100
    print("Grand Total: " + str(Total)+ "\n")
    print("Grand Total with shipping cost: ", str(total_price_with_shipping_cost)+ "\n")
  

    #Writing the bills
    file = open(Customer_Name + "_" + str(getdate()) + ".txt", "w")  

    file.write("\n---------------------INVOICE---------------------\n")
    file.write("\n" + "Name: " + Customer_Name + "\n")
    file.write("Phone no.: " + str(Contact) + "\n")
    Date = date_and_time()
    file.write("Date: " + str(Date) + "\n\n")

    file.write("\n-----------------------------------------------------------------------------------------------------------")
    file.write("\n ID  \tLaptop Name  \tBrand  \tPrice  \tQuantity  \tCPU  \tGraphics  \n")
    file.write("-----------------------------------------------------------------------------------------------------------\n\n")

    Total = 0
    for index in range(len(add_to_cart)):
        ID = int(add_to_cart[index][0])
        Quantity = int(add_to_cart[index][1])
        Name = value[ID][0]
        Brand = value[ID][1]
        Price = int(value[ID][2].replace("$", "")) * Quantity
        CPU = (value[ID][4])
        Graphics = (value[ID][5])
        Total = Price * Quantity
        Total += Grand_Total
        
        file.write(str(index + 1) + "\t" + Name + "\t" + Brand + "\t" + str(Price) + "\t" + str(Quantity) + "\t" + CPU + "\t" + Graphics)
        file.write("\n\n")

    total_price_with_shipping_cost = Total + 100
    file.write("\n-----------------------------------------------------------------------------------------------------------\n\n")

    file.write("Grand Total: " + str(Total)+ "\n")
    file.write("Grand Total with shipping cost:  " + str(total_price_with_shipping_cost)+ "\n")
    file.write("\n\n-----------------------------------------------------------------------------------------------------------")
    file.write("\n        Thank you! The laptops have been SOLD successfully.          \n")
    file.write("-----------------------------------------------------------------------------------------------------------\n")

    file.close()

