#Inventory System

def load_inventory(filename):
    print("Inventory System\n")
    print("="*50)
    print(f"Loading iventory from: {filename}\n")
    with open(filename, 'r') as file: 
        content = file.readlines()# Reads a text file with product data (one product per line)
        list_dict={} # empty dictionary
        global products
        products = [] # empty products lis
        for line in content: # loops through each line of the file
            if line == '\n': # skips newlines
                continue
            else:
                items = line.strip().split(',') # strips the line and seperates items.
                list_dict={'Product':items[0],'Qty':int(items[1]),'Price':float(items[2])} #updates dictionaryies
                products.append(list_dict) #Creates list
        return(products)
            
def display_inventory(products): # Displays all products in a formatted table
    print("Current Inventory:\n")
    print("Product Qty\tPrice\tValue\n")
    print("-"*50,'\n')
    for product in products:
        name = product['Product']
        qty = product ['Qty']
        price = product ['Price']
        global value
        value = qty * price
    
        print(f'{name}   {qty}\t{price}\t{value}\n')
    print("-"*50,'\n')
        
def find_product(products,name):
    print(f'Search for "{name}":\n')
    for product in products:
      if name.lower() == product['Product'].lower():
          print (f"Found!\nQuanity:{product['Qty']}, Price: ${product['Price']}.\n")
          return(product)
    
    print("None") 
    return None

def calculate_total_value(products):
    total = 0
    for product in products:
        value = product['Qty']*product['Price']
        total = total + value
    print(f"Total Inventory value:\n {total}")
    
def save_report(products,filename):
    with open(filename, 'w')as file:
        file.write(f"{load_inventory('inventory.txt')}")
        file.write(f"{display_inventory(products)}")
        file.write(f"{calculate_total_value(products)}")
        file.write(f"{find_product(products,'Mouse')}")
        print(f'Report saved to:\n{filename}')
        
load_inventory('inventory.txt')

