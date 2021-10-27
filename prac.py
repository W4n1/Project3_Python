user_name = input("Welcome user, please enter your name:\n")
user_input = input(f'Hi {user_name}, WELCOME! Converting months or days to'
                    'unites, please choose? Choose by typing'
                    '"months" or "days"\n')
if user_input == "months" or user_input == "month":
    from main import validate_and_execute_months
    validate_and_execute_months()Wan
elif user_input == "days" or user_input == "day":
    from main import validate_and_execute_days
    run_days_function = validate_and_execute_days()
else:
    print(f"{user_name}You must enter months or days in order to proceed")
