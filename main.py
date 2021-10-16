months_to_units = "31.5"
days_to_units = "30"
durartion_type = [months_to_units, days_to_units]
name_of_units = ["hours", "minutes", "seconds"]


def days_to_units_calc(custom_message, number_of_days):
    print(f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[0]}")
    print(f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[1]}")
    print(f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[2]}")


    '''print(custom_message)
days_to_units_calc("You have converted days to your preferred unit, please see results below", 35)'''

input("Please enter a number of days you'd like to convert to units\n")


def months_to_units_calc(customer_message,number_of_days):
    print(f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[0]}")
    print(f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[1]}")
    print(f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[2]}")


''' print(customer_message)
months_to_units_calc("You have converted months to your preferred unit", 35)'''

input("Please enter a number of months you'd like to convert to units\n")