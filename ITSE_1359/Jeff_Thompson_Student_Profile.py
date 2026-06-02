#Jeff Thompson  14 May 2026   Student Profile Card Generator

"""Create a Student Profile Card Generator that
that collects information from the user, processes it, 
and generates a formatted profile card."""

line_break="************************************************************" #Line  break variable for formatting.
print(line_break)

print("\n\t****STUDENT PROFILE CARD GENERATOR****\n")
print(line_break)


print("""\nWelcome to the Student Profile Card Generator!
This program will collect student information to 
create their profile card.\n""") #Escape character and new line for spacing.

#DATA COLLECTION

print("Please Enter your information to the following prompts:")
fname=input("First Name: ") # String inputs for the first and last name
lname=input("Last Name: ")
YOB=int(input('"Four Digit" Year of birth: ')) #Integer Type
ST =input('"Two Letter" State of residence: ') #Outside single quotations to display the double quotation marks around the emphasized words.
GPA=float(input("Current GPA: ")) #Float Type
FAV=input("Your Favorite programming language: ")
ID=str(input("Student ID number: "))
print("")
print(line_break)
print("")
print("Processing Data\n\nPrinting Card Shortly....")

#DATA PROCESSING
appx_age=2026-YOB #Current year 2026 minus entered year
full_name = f"{fname.title()},{lname.title()}"# Combining first and last name 
ST=ST.upper() #All uppercase method
GPA=f"{GPA:.2f}"#:.2f formats and displays two decimal places
email=f"{fname.lower()}.{lname.lower()}@student.edu"#Lower case methods for the email address.

#PROFILE CARD DISPLAY (a visually formated card)
print(f"\n{line_break}")
print("\n\t****STUDENT PROFILE CARD****\n")
print(f"* Name: {full_name.title()}")
print(f"* Student ID: {ID}")
print(f"* Age: {appx_age}")
print(f"* State of Residence: {ST}")
print(f"* Current GPA: {GPA}")
print(f"* Favorite Programming Language: {FAV.title()}")
print(f"* Student Email: {email}\n")

#SUMMARY STATISTICS
print(line_break)
print("\n\t****QUICK STATS****\n")
print(line_break)
print(f"\nTotal # of Characters in the Full Name is :{len(full_name)}")# Len function to count the characters and spaces
print(f"The # of letters int he firstname is: {len(fname)}")#Len function to count the characters
f_ini=[]# Empty Lists to capture characters
l_ini=[]
for letter in fname: #For loop to seperate charachters
    f_ini.append(letter) #Seperates the letters and adds them to the empty lists
for letter in lname:
    l_ini.append(letter)
print(f"Initials: {f_ini[0].upper()}{l_ini[0].upper()}")#Prints the first letter of each list.

print("\nThank you for using the Student Profile Card Generator, Happy Study's\n")
print(line_break)
