# contact_manager.py

contacts = { }# a empty dictionary to store contacts (name as key, phone as value)

def add_contact(contacts,name,phone): # Add Contact function
    contacts[name]=phone #assigns new phone value to name key
    for k,v in contacts.items(): # Loops through the dictionary
        print(f"Added: {k} - {v}") #Prints contacts as they are added.

def get_contact(contacts,name): #Retrieve contacts from dictionary
       print(f"Looking up {name}:")
       contact = contacts.get(name)# stores get function in contact variable
       if contact: # If contact variable is true
            print(contact) # Print the value
       else:
           print('Contact not found')

def display_all_contacts(contacts): #Loops through and displays all contacts
     for k,v in contacts.items():
          print(f"{k}: {v}")


def count_contacts(contacts):
    return(len(contacts))


print("Contact List Manager\n\n",'='*25,'\n')
add_contact(contacts,'Alice','555-1234')
add_contact(contacts,'Bob','555-5678')
add_contact(contacts,'Carol','555-9012')

print("\n All Contacts:\n")
display_all_contacts(contacts)

print(f"\nTotal Contacts: {count_contacts(contacts)}\n")

get_contact(contacts,'Bob')
print()
get_contact(contacts,'Dave')





