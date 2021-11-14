calc_to_hours = 24  # 24hours in a day
calc_to_minutes = 60  # minutes in an hour
calc_to_seconds = 3600   # seconds in an hour
name_unit = "hours", "minutes", "seconds" # will be used for when out putting data to person.

def main(user_input):
    user_input = ""

    def months_to_units(unit_chosen):
        # hour
        if unit_chosen == "hours":
            months_to_convert = input(f'{user_name}, you have selected months and hours, please enter number of '
                                      f'month(s) you would like to be converted:\n')
            month_hours(int(months_to_convert)) #try except to check a number or not

        # minute
        elif unit_chosen == "minutes":
            # month_minutes ()
            months_to_convert = input(f'{user_name}, you have selected months and minutes, please enter number of '
                                      f'month(s) you would like to be converted:\n')
            month_hours(int(months_to_convert))

        # seconds
        elif unit_chosen == "seconds":
            # month_seconds()
            months_to_convert = input(f'{user_name}, you have selected months and seconds, please enter number of months'
                                      f' you would like to be converted:\n')
            month_seconds(int(months_to_convert))
        else:
            return "Please enter months or days"


    def month_hours(num_months):
        if num_months > 0:
            return f"{num_months} months are {num_months * calc_to_hours} {name_unit[0]}"
        else:
            input(f'You entered a negative value, so no conversion for you!\n'
                  f'Do you want to start again?\n').lower()
            if user_input == 'yes':
                main()
            else:
                exit()
    # call function

    def month_seconds(num_months):
        if num_months > 0:
            return f'{num_months} months are {num_months * calc_to_seconds} {name_unit[1]}'

            pass


    def days_to_units(unit_chosen):
        unit_chosen = input("hours or hour or minute or minutes, or seconds or second")
        # hour
        if unit_chosen == "hours":
            days_to_convert= input(f'{user_name}, you have selected days and hours, please enter number of month(s) you would like'
                                   f'to be converted:\n')
            day_hours(int(days_to_convert))

        elif unit_chosen == "minutes":
            return (f'Thank you {user_name}, you have selected days and hours, please enter the number of days you would'
                    f'like for me to convert:\n')
            # minute

        # minute
        elif unit_chosen == "minutes":
            # day_minutes ()
            return (f'Thank you{user_name}, you have selected days and minutes, please enter the number of days you would'
                    f' like for me to convert:\n')

        # seconds
        else:
            unit_chosen == "seconds" or unit_chosen == "second"
            # day_seconds()
            return (f'Thank you {user_name}, you have selected days and seconds, please enter the number of days you would'
                    f'like for me to convert:\n')


    def day_hours(num_days):
        if num_days > 0:
            return f"{num_days} months are {num_days * calc_to_hours} {name_unit[0]}"
        else:
            return "You entered a negative value, so no conversion for you!"


    # intro
    user_name = input("Welcome Friend "
                      "please enter your name:\n")
    user_input = input(f'Hi {user_name}, WELCOME :) !\n'
                       f'Would you like to convert months or days?\n'
                       f'Enter months or days\n')

    # entering days or months

    if user_input == 'months' or user_input == 'days':
        print(f'You have selected {user_input}!'
              'What unit would you like to be converted\n '
              'hours\n minutes \n seconds?')
        unit_chosen = input()
    # user has chosen a period

        while unit_chosen != "hours" and unit_chosen != "minutes" and unit_chosen != "seconds":
            unit_chosen = input("please enter minutes, hours or seconds")
        months_to_units(unit_chosen)
    # anything that is not house, minutes or seconds should send the input above.


    elif user_input == 'days' or user_input == "months":
        print(f'You have selected {user_input}!'
              'What unit would you like to be converted\n '
              'hours\n minutes \n seconds?')
        unit_chosen = input()
        days_to_units(unit_chosen)

    else:
        print("Please enter months or days to proceed next time!")


main(user_input="")


'''return (f"{unit_chosen} months are {unit_chosen * calc_to_hours}name_unit[0]")

        # call function for the calculations for months and hours

    elif unit_chosen == 'minutes' or unit_chosen == 'minute':
        print(f 'you have selected months and minutes, please enter number of months you would like to be converted:\n')
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



# need to create the calculations - accepting user input
