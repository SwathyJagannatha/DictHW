from colorama import Fore, Back, Style
from termcolor import colored

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket):
    count = len(service_tickets.keys())
    print("No of keys",count)
    user_name = input("Enter your name")
    user_issue = input("Please enter the issue you are facing!")
    ticketnumber = count+1
    key = "Ticket00" + str(ticketnumber)
    print("key is",key)
    
    service_tickets[key] = {"Customer" : user_name , "Issue" : user_issue,"Status" : "open"}
    print(service_tickets)
    pass

def status_update(ticket):
    ticket_val = input("Enter the Existing ticket number,for which you want the status to be updated")
    print(f"Updating the status of existing open ticket - {Fore.GREEN}{ticket_val}:")
    print(Style.RESET_ALL)
    ticket_val = ticket_val.strip()
    if ticket_val in ticket:
        if ticket[ticket_val]["Status"] == "open":
            ticket[ticket_val]["Status"] = "closed"

        print("Service Tickets after status update:")
        display_ticket(ticket)
        print(Style.RESET_ALL)

    else:
        print("Sorry,ticket doesnt exist! Please enter existing ticket!")
    pass

def remove_ticket(ticket):
   
    ticket_val = input("Enter the Existing ticket number which you wish to delete")
    ticket_val = ticket_val.strip()

    if ticket_val in ticket:
        del ticket[ticket_val]
        print(f"Ticket {ticket_val} successfully deleted")
        display_ticket(ticket)
    else:
        print(f"Sorry ticket {ticket_val} does not exist")
    pass

def display_ticket(ticket):
    for ticket,details in ticket.items():
        print(f"{Fore.LIGHTGREEN_EX}Here are the various parameters for the {ticket} - service request categories: ")
        print(Style.RESET_ALL)
        for item,value in details.items():
            print(f" - {Fore.MAGENTA}{item} : {Fore.YELLOW}{value}")
            print(Style.RESET_ALL)
    pass

def filter_by_status(menu):
    ticket_status = input("Enter the status by which you want to filter tickets displayed!!").lower()
    if ticket_status in ["open","closed"]:
        for key,value in menu.items():
            if value["Status"].lower()== ticket_status.lower():
                print(f"{Fore.LIGHTBLUE_EX}TicketId : {key} , {Fore.GREEN}Customer : {value['Customer']} , {Fore.LIGHTYELLOW_EX}Issue : {value['Issue']} , {Fore.MAGENTA}Status :{value['Status']}")
        print(Style.RESET_ALL)
    else:
        print("Please enter open/closed for status filtering!!")
    pass

def main(ticket):
    while True:
        response =  input("""What would you like to do? 
                          1. Open a new service ticket.
                          2. Delete a ticket
                          3. Display all tickets
                          4. Update the status of an existing ticket to "closed". 
                          5. Filter By Status 
                          6. Quit\n""")

        if response  == "1":
            response = input("Do you want to add a new service ticket?\n")
            open_ticket(ticket)
        elif response == "2":
            response = input("Do you want to remove ticket?\n")
            remove_ticket(ticket)
        elif response == "3":
            response =input("Do you want to view the existing service tickets?\n")
            display_ticket(ticket)
        elif response == "4":
            response =input("Do you want to Update the status of existing ticket to closed?\n")
            status_update(ticket)
        elif response == "5":
            filter_by_status(ticket)
        elif response == "6":
            print("Exiting...")
            break
        else:
            print("Please enter a valid response!")
    pass

main(service_tickets)