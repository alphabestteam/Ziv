from customer import Customer
from register import Register, product_receiver, choice_manager

current_customer = Customer(input("Welcome to the supermarket! Enter your name: "))
open_register = Register()
closed_register = Register()
selected_choice = 0
while selected_choice != 3:
    selected_choice = choice_manager()
    match selected_choice:
        case 1:
            try:
                product_name, product_units = product_receiver()
            except:
                continue
            current_customer.add_product(product_name, product_units)
        case 2:
            try:
                product_name, product_units = product_receiver()
            except:
                continue
            current_customer.remove_product(product_name, product_units)
        case -1:
            continue
open_register.checkout_customer(current_customer)
open_register.print_summary()
