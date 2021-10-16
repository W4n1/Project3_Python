
def days_to_units(num_of_days, conversion_unit):    # defining the unites to days
    # how many hours are in a (n) of days
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"

    # how many minutes are in a (n) of days
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 1440} minutes"

    # how many seconds are in a (n) of days
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 86400} seconds"
    else:
        return "unsupported unit"


def months_to_unit(num_of_months, conversion_unit):  # defining unites to months
    # how many hours are in a (n) of month(s)
    if conversion_unit == "hours":
        return f"{num_of_months} days are {num_of_days * 24} hours"

    # how many minutes are in a (n) of month(s)
    elif conversion_unit == "minutes":
        return f"{num_of_months} days are {num_of_days * 1440} minutes"

    # how many seconds are in a (n) of month(s)
    elif conversion_unit == "seconds":
        return f"{num_of_months} days are {num_of_months * 86400} seconds"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"], months_to_unit_dictionary["unit2"])

            print(calculated_value)

        elif user_input_number or user_input_month == 0:
            print("you entered 0, please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you!")
    except:
        print("You're input is not constructive, try again. Don't ruin my program!")


users_name = ""
user_input = ""
users_name = input("Hi user, please input your name:\n")
while user_input != "exit":
    user_input = input(f"Hi {users_name}, which would you like to convert to unites? {months_to_unit} or {days_to_units}?\n")

    user_input = input(f"Thank you {users_name}, please enter a number of days or months and a conversion unit!\n")
    days_and_unit_dictionary = user_input.split("day:hours:minutes")
    print(days_and_unit_dictionary)
    days_and_unit_dictionary = {"days": days_and_unit_dictionary[0], "unit": days_and_unit_dictionary[1]}
    print(days_and_unit_dictionary)

    validate_and_execute()  # calling the validate and execute function



'''funtions we have used 
- print("some text") : prints standard output on to the console log
- input ("enter value") : asks user for input
- set ( 1, 2, 3, 4) : takes a list and converts it to a set
- int("30"): converts value into an integer number 
- datatype.built-infunction() i.e. .split() : there are many functions like this

There are a lot of built in functions
We can create our own functions

syntax of a dictionary is > {"days": 20, "unit":'hours'} days and unit are keys and 20 and hours are the values. 
The syntax above is to then be assigned with a variable'''
