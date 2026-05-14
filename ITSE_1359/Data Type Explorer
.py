#Objective: Create a script that demonstrates different data types and conversions.

"""Create variables with the following values: 
An integer: 42
A float: 3.14159
A string containing a number: "100"
A boolean: True
A string: "Python"
Display the data type of each variable using type()
Perform and display the following conversions: 
Integer to float
Float to integer (note what happens)
String to integer (for the string containing a number)
Integer to string
Boolean to integer
Integer to boolean (try with 0 and 1)
Try some operations across types and display the results: 
Integer + float
String + string
String * integer
Try string + integer (with and without conversion)"""

num_int = 66
num_flt = float(75)
num_str = "105"
is_on = True
name ="Python"

print(f"\nThis variable is a {type(num_int)}")
print(f"\nThis variable is a {type(num_flt)}")
print(f"\nThis variable is a {type(num_str)}")
print(f"\nThis variable is a {type(is_on)}")
print(f"\nThis variable is a {type(name)}")

print(f"\nThis integer as a float is:{float(num_int)}")
print(f"\nThis float as a integer is:{int(num_flt)}")
print(f"\nThis string as a integer is: {int(num_str)}")
print(f"\nThis boolean as a integer is {int(is_on)}")
print(f"\nThis integer as a boolean is {bool(0)}")
print(f"\nThis integer as a boolean is {bool(1)}")

print(f"\nThis Integer + float is:{num_int+num_flt}")
print(f"\nThis String + this other string is {name + num_str}")
print(f"\nThis is a string multiplied {(name + ' ')*5}")
print(f"\nThis is a string combined with an integer {int(num_str) + num_int}")
print(f"\nThis is a string combined with an integer {num_str + num_int}")
