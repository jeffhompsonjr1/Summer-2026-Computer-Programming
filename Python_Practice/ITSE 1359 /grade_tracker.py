grades = [] # Empty list to 
def add_grade(grades,new_grades):
    for grade in new_grades:
        grades.append(grade)
    return(grades)

def calculated_average(grades):
    return((sum(grades))/len(grades))

def find_highest(grades):
    return(max(grades))

def find_lowest(grades):
    return(min(grades))

def display_summary(grades):
    print("Student Grade Summary\n")
    print("="*20,'\n')
    print(f'All grades: {grades}\n')
    print(f'Number of grades: {len(grades)}\n')
    print(f'Average grade: {calculated_average(grades)}\n')
    print(f'Highest grade: {find_highest(grades)}\n')
    print(f'Lowest grade: {find_lowest(grades)}')

new_grades=[85, 92, 78, 95, 88]

add_grade(grades,new_grades)
display_summary(grades)