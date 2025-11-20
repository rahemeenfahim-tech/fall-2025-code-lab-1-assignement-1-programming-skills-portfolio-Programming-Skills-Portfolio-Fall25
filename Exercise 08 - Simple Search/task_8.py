Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]         #Create a list with these listed names


for name in Names:
    if name.lower() == "sam":                                        # check if sam exsists as a name in the list
        print("Sam was found in the list!")                  # Print this statement if sam exsists as a name in the list
        break
else:
    print("Sam was not found in the list.")                 # Or else print this statement


search_name = input("Enter the name you want to search: ")  #Ask the user to input the name they are searching for


for name in Names:
    if search_name.lower() == name.lower():                                   #If the users input name matches the name in the list
        print(f"{search_name} was identified from the list!")        #Print this statement
        break
else:
    print(f"{search_name} was not identified the list.")  #if the person is not there in the list, this statement will be printed
    