#Create a simple report file
student_name = "Jeff Thompson"
scores = [85,92,78,95,88]
average = sum(scores)/len(scores)

with open("student_report.txt",'w')as file:
    file.write("Student Grade Report\n")
    file.write("=" * 25 + "\n")
    file.write(f"Student: {student_name}\n")
    file.write(f"Scores: {scores}\n")
    file.write(f"Average: {average:.1f}\n")

    if average >=90:
        file.write("Grade: A\n")
    elif average >= 80:
        file.write("Grade: B\n")
    elif average >= 70:
        file.write("Grade: C\n")
    elif average >= 60:
        file.write("Grade: D\n")
    else:
        file.write("You have failed")
with open('student_report.txt')as file:
    print(file.read())

print("Report saved to student_report.txt")


  
  