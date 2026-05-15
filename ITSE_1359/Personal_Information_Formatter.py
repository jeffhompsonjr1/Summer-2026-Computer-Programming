#Personal Information Formatter

"""Create a script that collects personal
information and displays it in multiple formats."""

#Create a script that asks the user for the following information:

print("Fill in personal information:")
name = input("Name: ")
age = int(input("Age: "))
HT = float(input("Height (in Meters): "))
WT = float(input("Weight (in KGs):  "))
job = input("Occupation: ")
line_break=("**************************************************************")
#calculate the BMI (Body Mass Index) using the formula: BMI = weight / (height * height)
BMI = WT/(HT*WT)

#Format 1 - Summary: A neatly formatted box with labels
print(f"\n\t ***Format 1 - Summary***\n")
print(line_break)
print(f"\nName:{name.title()}\tAge: {age:.2f}, years old")
print(f"Height: {HT:.2f} m   \tWeight:{WT:.2f} kg") 
print(f"BMI: {BMI:.2f}%      \tOccupation: {job.title()}\n")
print(line_break)
#Format 2 - Database Entry: Each piece of information on a new line with labels
print("\n\t ***Format 2 - Database Entry***\n")
print(line_break)
print(f"\nName: {name.title()}")
print(f"Age: {age:.2f}, years old")
print(f"Height: {HT:.2f} m\nWeight:{WT:.2f} kg") 
print(f"BMI: {BMI:.2f}% ")
print(f"Occupation: {job.title()}\n")
print(line_break)
#Format 3 - One-liner: All information in a single line with semicolons as separators
print("\n\t ***Format 3 - One-Liner***\n")
print(line_break)
print(name,age,HT,WT,BMI,job,sep=" ;")
print(line_break)





