correct_password = 12345                                  #The correct password set by us
attempts = 0                                              #the total number of attempts so far

while attempts<5:                                         #When the attempts are less than 5 and attempts is 0
    password=int(input("Enter the password:"))            #this statement is printed to the user

    if password == correct_password:                      #If the password entered by the user is the same as the correct password
        print("Congratulations! You have logged in successfully")    #This statement will be printed
        break                                             #Exit the loop once the condition is met
    else:                                                 #When the condition is not met
        attempts += 1                                     #The number of attempts will be increased
        attempts_left = 5-attempts                        #This shows the number of attempts left
        print(" Oh no! your Access is Denied, try again. You have", attempts_left, "attempts remaining!") #when the password is wrong this statement will be printed

if attempts == 5:                                         #When the attempts is more than 5, the loop will eventually be stopped
    print("You have reached the maximum number of attempts. The Authorities have been alerted ") #This would be final statement since they couldn't crack the password