months_to_units = 31  # maybe do it by month rather than a estimate
days_to_units = 30
durartion_type = [months_to_units, days_to_units]
name_of_units = ["hours", "minutes", "seconds"]


def days_to_units_calc(number_of_days):
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[0]}")
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[1]}")
    return (f"{number_of_days} days are {number_of_days * durartion_type[1]} {name_of_units[2]}")


def months_to_units_calc(number_of_months):
    if number_of_months > 0:
        return (f"{number_of_months} months are {number_of_months * durartion_type[0]} {name_of_units[0]}")
        return (f"{number_of_months} months are {number_of_months * durartion_type[0]} {name_of_units[1]}")
        return (f"{number_of_months} months are {number_of_months * durartion_type[0]} {name_of_units[2]}")


def validate_and_execute_days():
    try:
        user_input_integer = int(user_input1)
        if user_input_integer > 0:
            calculated_value = days_to_units_calc(user_input_integer)
            print(calculated_value)
        elif user_input1 == 0:
            print("You entered a 0, please enter a valid positive number"
                  "of days")
        else:
            print("You have entered a negative number of days, please enter a"
                  "valid positive number in order to proceed")
    except ValueError:
        print("Your input is not a number of days. To proceed please use a"
              "number! Do not ruin my program friend!")



def validate_and_execute_months():
    try:
        user_input_integer = int(user_input1)
        if user_input_integer > 0:
            calc_value = months_to_units_calc(user_input_integer)
            print(calc_value)
        elif user_input1 == 0:
            print("You entered 0, please enter a valid positive number"
                  "of months to proceed")
        else:
            print("You entered a negative number of months, please enter"
                  "a valid positive number")
    except ValueError:
        print("Your input is not a number of months. To proceed please use"
              "a number! Do not ruin my program friend!")


# looping the logic
# assign an empty string to variable user_input before the while
user_input1 = ""
while user_input1 or user_input != "exit":
    if user_input1 == "days" or user_input1 == "day":
        user_input1 = input(f"Please enter a number of day(s) you'd like me to"
                            "convert to units!\n")
        validate_and_execute_days()
    else:
        user_input1 == "months" or user_input1 == "month"
        user_input1 = input(f"Please enter a number of month(s) you'd like me"
                            "to convert to units!\n")
        validate_and_execute_months()
print('Please enter month(s) or day(s)-\n')


'''
> currently it is only converting hours. 
> there is no real transaction from days to months
> for the day loop, exit currently means change to months
> for the month loop, exit finishes the process. 
> I need to apply the intro in the test section to the this file
'''
