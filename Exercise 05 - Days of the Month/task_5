Month_days ={1:31,                            #Creating a dictionary of the 12 months as keys with days as values.
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}

days_month = int(input("Enter a month number (1-12): ")) #Ask the user to input a valid month number from the range of 1 to 12
if 1 <= days_month <=12:                                 # Check if the month number is valid (between 1 and 12)
    if days_month == 2:                                   # if the month is February
        leap = input("Is it a leap year? (yes/no): ")      # Ask the user if it's a leap year

        if leap.strip().lower() == "yes":                             # Approve different ways the user might type "yes" and any spaces are removed though the strip function
            print("February has 29 days.")                    #Leap year
        else:
            print("February has 28 days.")                     # Not a leap year

    else:
        print(f"The month {days_month} has {Month_days[days_month]} days.")   # For all months, print days from dictionary

else:
    print("Please enter a number between 1 and 12.")            # If the month number is not between 1 and 12 display this to the user/