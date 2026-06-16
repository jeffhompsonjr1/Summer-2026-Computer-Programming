import re

text = '''Contact us at 555-1234 or 555-5678.

We have 25 items in stock.

Prices: $19.99, $5.50, and $100.00.'''

print("Pattern Finder\n\n",'='*30)

def find_phone_numbers(text): # Returns a list of all found phone numbers
    pattern = r"\d\d\d-\d\d\d\d"
    phone_numbers = re.findall(pattern, text)
    print("\nPhone Numbers found:\n")
    for numbers in phone_numbers:
        print(numbers,"\n")

def find_all_numbers(text): # Returns a list of all found numbers
    pattern = r"\d+"
    all_numbers = re.findall(pattern, text)

    print(f"\nAll numbers found:\n\n {all_numbers}")

def find_prices(text): # Returns a list of all found prices.
    pattern = r"\$\d+\.\d\d"
    prices = re.findall(pattern, text)
    print("\nPrices found:\n")
    for price in prices:
        print(price,'\n')





find_phone_numbers(text)
find_all_numbers(text)
find_prices(text)

