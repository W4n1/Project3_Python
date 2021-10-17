
months_to_units = 31.5
days_to_units = 30
durartion_type = (months_to_units, days_to_units)
name_of_units = ("hours", "minutes", "seconds")


def days_to_units_calc(number_of_days):
    if number_of_days > 0:
        return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[0]}")
        return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[1]}")
        return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[2]}")
    else:
        return "you have entered a negative value, please enter a positive to proceed."
    
    
'''print(custom_message)
days_to_units_calc("You have converted days to your preferred unit, please see results below", 35)'''


user_day_input = input("Please enter a number of days you'd like me to convert to units!\n")
user_input_integer = int(user_day_input)
calc_value = days_to_units_calc(user_input_integer)
print(calc_value)


def months_to_units_calc(number_of_days):
    if number_of_days > 0:
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[0]}")
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[1]}")
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[2]}")
    else:
        return "you have entered a negative value, please enter a positive to proceed."



'''print(customer_message)
months_to_units_calc("You have converted months to your preferred unit", 35)'''

user_month_input = input("Please enter a number of months you'd like me to convert to units!\n")

user_input_integer = int(user_month_input)
calc_value = months_to_units_calc(user_input_integer)
print(calc_value)  


