import sys
import os

# ----------------------------------------------
# Importing data from txt file
# Clear Screen
# Validation - Numbers, No input
# Option 4 - Search based on price of products
# ----------------------------------------------

products_data = []
f = open("products.txt","r") # Open and reading the txt file
for line in f:
    l = line.strip() # Remove all "\n" = lines will be stripped on runs of whitespace
    products_data.append(l) # Append data of l as products_data list
products = [products_data[x:x+4] for x in range(0, len(products_data), 4)] # Slicing & creating 2D products list for every 4 lines

f.close() # Close the txt file

selections = [
    "1. Display all Food Products",
    "2. Display Food Full Names for selection",
    "3. Search based on Name or Category Substring",
    "4. Search based on Price Range",
    "Q. Press Q to quit" 
]

s1_options = [
    "Enter N for Next Product",
    "Enter P for Previous Product",
    "Enter M to Return to Main Menu"
]             

s3_options = [
    "1. Search again",
    "2. Return to Main Menu"
]

s4_options = [
    "1. Search with another Price Range",
    "2. Return to Main Menu"
]

def clear(): # Clear screen
    if os.name == "nt":
        os.system("cls")
    elif os.name == "mac" or os.name == "posix":
        os.system("clear")

def input_number(message): # Test for ints only for userinput
    while True:
        try:
            UserInput = int(input(message))
        except ValueError:
            print("This is an invalid entry. Please try again.")
            continue
        else:
            return UserInput 

def input_float(message): # Test for floats only for userinput
    while True:
        try:
            UserInput = float(input(message))
        except ValueError:
            print("This is an invalid entry. Please try again.")
            continue
        else:
            return UserInput 
             

print("Welcome!")

while True:
    print("\nMain Menu", "\n------------")
    for item in selections:
        print(item)
    target=input("\nPlease input your selection: ")

    if not target: # Prevent empty userinput
        print("Error: Nothing was selected.")
        continue

    if target=="1": # Food Products Section
        print("You have selected:", int(target), "\n")

        product_index = 0 # Initial Product Index counter
        product_no = 1 # Initial Product Number counter

        while True:
            print("\nProduct", product_no, "of", len(products)) # Display Products
            print("-------------------------------------------------",
                "\nName: ", products[int(product_index)][0], 
                "\nCategory: ", products[int(product_index)][1],
                "\nDescription: ", products[int(product_index)][2], 
                "\nPrice: ", "$", products[int(product_index)][3],
                "\n-------------------------------------------------")
            
            if product_no == len(products): # Last Product
                print ("Enter N to Return to First Product")
                print (s1_options[1])
                print (s1_options[2]) 
            
            elif product_no == 1: # First Product
                print (s1_options[0])
                print (s1_options[2])  
            
            else: # All valid Products in list
                for item in s1_options:
                    print(item)

            while True:
                opt_target=input("")

                if not opt_target: # Prevent empty UserInput
                    print("Error: Nothing was selected. Please try again.")
                    continue

                elif opt_target=="N": # Display "N"ext product
                    if product_no > len(products): # Invalid
                        print("This is an invalid option. Please try again.")
                        continue
                    
                    elif product_no == len(products): # Last product
                        product_index = 0
                        product_no = 1
                        break

                    elif product_no >= 1: # All valid products in list
                        product_index += 1
                        product_no += 1
                        break

                    else:
                        break
                
                elif opt_target=="P": # Display "P"revious product
                    if product_no <= 1:
                        print("This is an invalid option. Please try again.") # If current display is 1st product, don't allow Previous option
                        continue
                    elif product_no > len(products):
                        print("This is an invalid option. Please try again.") # Product no. shouldn't be more than length of products
                        continue
                    else:
                        product_index -= 1
                        product_no -= 1
                        break
                
                elif opt_target=="M": # Return to Main "M"enu
                    clear()
                    break

                else:
                    print("This is an invalid option. Please try again.")
                    continue

            if opt_target=="M":
                break
            else:
                continue
         


    elif target=="2":
        print("You have selected:", int(target), "\n") # Full Product Names Section

        while True:
            print("Food Products", "\n------------")
            for i in range(len(products)):
                    print(i+1, end=". ")
                    print(products[i][0])

            opt_target2 = input_number("\nPlease input your selection: ")

            if not opt_target2: # Prevent empty UserInput
                print("This is an invalid option. Please try again.")
                continue
       
            elif 0 < int(opt_target2) <= len(products):
                print("\nProduct", int(opt_target2), "of", len(products)) # Display Full Products of Input Choice
                print("-------------------------------------------------",
                    "\nName: ", products[int(opt_target2)-1][0], 
                    "\nCategory: ", products[int(opt_target2)-1][1],
                    "\nDescription: ", products[int(opt_target2)-1][2], 
                    "\nPrice: ", "$", products[int(opt_target2)-1][3],
                    "\n-------------------------------------------------")
                print("Enter P to return to Previous Menu")
                print("Enter M to return to Main Menu")

                while True:
                    opt2_target2=input("")
                    if not opt2_target2: # Prevent empty UserInput
                        print("Error: Nothing was selected.")
                        continue 

                    elif opt2_target2=="P": # Return to "P"revious Menu
                        break
                    
                    elif opt2_target2=="M": # Return to "M"ain Menu
                        clear()
                        break

                    else:
                        print("This is an invalid option. Please try again.")
                        continue
                
                if opt2_target2=="M":
                    break
                else:
                    continue
                
            else:
                print("This is an invalid option. Please try again.")
                continue



    elif target=="3":
        print("You have selected:", int(target), "\n")
        
        while True:
            search_list = []
            search_item = input("\nPlease enter your search input: ")

            if not search_item: # Prevent empty UserInput
                print("Error: There is no input.")
                continue

            else:
                for index in range(len(products)):
                    if search_item.lower() in products[index][0].lower() or search_item.lower() in products[index][1].lower():
                        search_list.append(products[index])
                
                if len(search_list) == 0: # If no results returned from the appended list above:
                    print("We do not have '%s'. \n\nYou may like to: " % search_item)
                else:
                    for index in range(len(search_list)):
                        print("\nProduct", str(index+1), "of", (len(search_list)))
                        print("-------------------------------------------------",
                            "\nName: ", search_list[index][0], 
                            "\nCategory: ", search_list[index][1],
                            "\nDescription: ", search_list[index][2], 
                            "\nPrice: ", "$", search_list[index][3],
                            "\n-------------------------------------------------")
                for item in s3_options:
                    print(item)
                
                while True:
                    opt_target3 = input("\nPlease input your selection: ")

                    if not opt_target3: # Prevent empty UserInput
                        print("Error: Nothing was selected.")
                        continue
                    
                    elif opt_target3=="1": # Continue Search
                        break
                        
                    elif opt_target3=="2": # Return to Main Menu
                        clear()
                        break
                    
                    else:
                        print("This is an invalid option. Please try again.")
                        continue
            
            if opt_target3=="1":
                continue
            else:
                break



    elif target=="4": # Search by Price range
        print("You have selected:", int(target), "\n")

        while True:
            price_list = []
            min_price = input_float("Please enter the minimum price: $ ")
            max_price = input_float("Please enter the maximum price: $ ")

            min_float = float(min_price)
            max_float = float(max_price) 
            print("\nSearching for products priced in range $", "{:.2f}".format(min_float), "to $", "{:.2f}".format(max_float), "...")  # Credits: https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python
        
            for index in range(len(products)):
                if min_float <= float(products[index][3]) <= max_float: # Check price as floats
                    price_list.append(products[index])

            if len(price_list) == 0:
                print("No products were found priced in the range.", "\n\nYou may want to:")

            else:
                for index in range(len(price_list)):
                    print("\nProduct", str(index+1), "of", len(price_list))
                    print("-------------------------------------------------",
                        "\nName: ", price_list[index][0], 
                        "\nCategory: ", price_list[index][1],
                        "\nDescription: ", price_list[index][2], 
                        "\nPrice: ", "$", price_list[index][3],
                        "\n-------------------------------------------------")

            for item in s4_options:
                print(item)

            while True:
                opt_target4 = input("\nPlease input your selection: ")

                if not opt_target4: # Prevent empty UserInput
                    print("Error: Nothing was selected.")
                    continue
                
                elif opt_target4=="1": # Continue Search
                    break
                    
                elif opt_target4=="2": # Return to Main Menu
                    clear()
                    break
                
                else:
                    print("This is an invalid option. Please try again.")
                    continue
        
            if opt_target4=="1":
                continue
            else:
                break

    elif target=="Q":
        break
    else: 
        print("This is an invalid selection. Please try again.")
        continue


print("\nHave A Nice Day, Goodbye!")