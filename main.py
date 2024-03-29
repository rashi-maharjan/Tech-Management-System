import operation
import read

# Creation of the main file starts from here
read.welcome_message()
is_running = True

while is_running:
    read.option_selected()

    option_selected = False
    while not option_selected:
        try:
            option = int(input("Enter an option: "))
            option_selected = True
        except:
            read.invalid_input()
            read.option_selected()

    if option == 1:
        operation.make_purchase()

    elif option == 2:
        operation.make_sell()

    elif option == 3:
        read.display_thanks()
        is_running = False

    else:
        read.invalid_input()
