months_to_units = 31.5  # maybe do it by month rather than a estimate
days_to_units = 30
durartion_type = (months_to_units, days_to_units)
name_of_units = ("hours", "minutes", "seconds")


def days_to_units_calc(number_of_days):
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[0]}")
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[1]}")
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[2]}")


'''print(custom_message)
days_to_units_calc("You have converted days to your preferred unit, please see results below", 35)'''


def validate_and_execute_days():
    try:
        user_input_integer = int(user_day_input)
        if user_input_integer > 0:
            calculated_value = days_to_units_calc(user_input_integer)
            print(calculated_value)
        elif user_day_input == 0:
            print("You entered a 0, please enter a valid positive number of days")
        else:
            print(
                "You have entered a negative number of days, please enter a valid positive number in order to proceed")
    except ValueError:
        print("Your input is not a number of days. To proceed please use a number! Do not ruin my program friend!")

#looping the logic
#assign an empty string to variable user_day_input before the while
user_day_input = ""
while user_day_input != "exit":
      user_day_input = input("Please enter a number of days you'd like me to convert to units!\n")
      validate_and_execute_days()


def months_to_units_calc(number_of_days):
    if number_of_days > 0:
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[0]}")
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[1]}")
        return (f"{number_of_days} months are {number_of_days * durartion_type[0]} {name_of_units[2]}")


'''print(customer_message)
months_to_units_calc("You have converted months to your preferred unit", 35)'''


def validate_and_execute_months():
    try:
        user_input_integer = int(user_month_input)
        if user_input_integer > 0:
            calc_value = months_to_units_calc(user_input_integer)
            print(calc_value)
        elif user_month_input == 0:
            print("You entered 0, please enter a valid positive number of months to proceed")
        else:
            print("You entered a negative number of months, please enter a valid positive number")
    except ValueError:
        print("Your input is not a number of months. To proceed please use a number! Do not ruin my program friend!")

# creating the loop 
user_month_input = ""
while user_month_input != "exit":
    user_month_input = input("Please enter a number of months you'd like me to convert to units!\n")
    validate_and_execute_months()



'''
> currently it is only converting hours. 
> there is no real transaction from days to months
> for the day loop, exit currently means change to months
> for the month loop, exit finishes the process. 
> I need to apply the intro in the test section to the this file
'''