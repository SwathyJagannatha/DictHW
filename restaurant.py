from colorama import Fore, Back, Style
from termcolor import colored

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_category(menu):
    restaurant_menu["Beverages"] = {"Expresso Freddo":7.99,"Mango Lassi":5.99}
    print("Printing the dict after addition of beverages")
    print(restaurant_menu)
    resp = input("Do you like to add some more varieties?\n").lower()
    if resp == "yes":
        restaurant_menu["Chats"] = {"Palak Chat":10.99,"Samosa Chat":7.99}
    print(restaurant_menu)
    pass

def price_update(menu):
    print("Updating price of Steak to 17.99")
    restaurant_menu["Main Course"]["Steak"] = 17.99
    print (restaurant_menu) 
    pass

def remove_item(menu):
   
    del menu["Starters"]["Bruschetta"]
    print("""Restaurant menu after delete operation:
          """)
    view_dict(menu)

    ans = input("Do you want to add item back?")
    if ans == "yes":
        menu["Starters"]["Bruschetta"] = 6.50

    print(menu)
    
    resp = input("Do you want to delete item again(pop func)?")
    if resp == "yes":
        pop_val = menu["Starters"].pop("Bruschetta",None)
    print(f"Popped item: Bruschetta, Value: {pop_val}")
    print(menu)
    pass

def view_dict(menu):
    for food,variety in menu.items():
        print(f"{Fore.LIGHTGREEN_EX}Here are the food varieties for the {food} categories: ")
        print(Style.RESET_ALL)
        for item,value in variety.items():
            print(f" - {Fore.MAGENTA}{item} : {Fore.YELLOW}{value}")
            print(Style.RESET_ALL)
    pass

def main(menu):
    while True:
        response =  input("What would you like to do? 1. add 2. remove 3. view 4.update 5.quit")

        if response  == "1":
            response = input("Do you want to add a new category BEVERAGES with atleast 2 items to the restaurant?\n")
            add_category(menu)
        elif response == "2":
            response = input("Do you want to remove BRUSCHETTA from Starters?\n")
            remove_item(menu)
        elif response == "3":
            response =input("Do you want to view the existing restaurant list?\n")
            view_dict(menu)
        elif response == "4":
            response =input("Do you want to Update the price of Steak to 17.99?\n")
            price_update(menu)
        elif response == "5":
            print("Exiting...")
            break
        else:
            print("Please enter a valid response!")
    pass

main(restaurant_menu)