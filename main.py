calc_to_hours = 24  # 24hours in a day
calc_to_minutes = 60  # minutes in an hour
calc_to_seconds = 3600   # seconds in an hour
name_unit = "hours", "minutes", "seconds"


def months_to_units(unit_chosen) -> object:
    # hour
    if unit_chosen == "hours" or unit_chosen == "hour":
        month_hours()
        return (f'{user_name}, you have selected months and hours, please enter number of months you would like '
                f'to be converted:\n')
    
    # minute
    elif unit_chosen == "minutes" or unit_chosen == "minute":
        # month_minutes ()
        return (f'{user_name}, you have selected months and minutes, please enter number of months you would like '
                f'to be converted:\n')
    
    # seconds 
    elif unit_chosen == "seconds" or unit_chosen == "second":
        # month_seconds()
        return (f'{user_name}, you have selected months and seconds, please enter number of months you would like '
                f'to be converted:\n')
    

def days_to_units(unit_chosen):
    # hour
    if unit_chosen == "hours" or unit_chosen == "hour":
        day_hours()
        return (f'{user_name}, you have selected months and hours, please enter number of months you would like '
                f'to be converted:\n')

    else:
        return "please enter months or days"


def month_hours(num_months):
    if num_months > 0:
        return f"{num_months} months are {num_months * calc_to_hours} {name_unit[0]}"



        '''return (f"{unit_chosen} months are {unit_chosen * calc_to_hours}name_unit[0]")

        # call function for the calculations for months and hours

    elif unit_chosen == 'minutes' or unit_chosen == 'minute':
        print(f'you have selected months and minutes, please enter number of months you would like to be converted:\n')
        # call function for the calculations for months and minutes

    elif unit_chosen == 'seconds' or unit_chosen == 'second':
        print('you have selected months and seconds, please enter number of months you would like to be converted:\n')
        # call function for the calculations for months and seconds


def months_to_units(unit_to_months):
    # hour
    if unit_to_months == "hours":
        return (f"{num_months} months are {num_months * calc_to_hours}name_unit[0]")

        # minute
    elif unit_to_months == "minutes"
        print(f"{num_months} months are {num_months * calc_to_minutes}name_unit[1]")

        # second
        print(f"{num_months} months are {num_months * calc_to_seconds}name_unit[2]")
    # months_to_units()  #calling the month function


# days_to_units()  #calling the day function


def days_to_units(num_days):
    print(f"{num_days} days are { num_days * calc_to_hours}name_unit[0]")
    print(f"{num_days} days are { num_days * calc_to_minutes}name_unit[1]")
    print(f"{num_days} days are { num_days * calc_to_seconds}name_unit[2]")
'''

user_name = input("Welcome Friend "
                  "please enter your name:\n")
user_input = input(f'Hi {user_name}, WELCOME :) !\n '
                    'Would you like to convert months or days? '
                    'Enter months or days\n')

# entering days or months
if user_input == 'months' or user_input == 'month':
    print('You have selected months!'
          'What unit would you like to be converted\n '
          'hours\n minutes \n seconds?')
    months_to_units(unit_chosen="hours" or "minutes" or "seconds")

else:
    user_input == 'days' or user_input == 'day'
    print('You have selected days!'
          'What unit would you like to be converted\n '
          'hours\n minutes \n seconds?')
    days_to_units(unit_chosen="hours" or "minutes" or "seconds")




# need to create the calculations - accepting user input
