# tasks = []

# tasks.append("Buy Grocieries")
# tasks.append("Finish Homework")
# tasks.append("Call Mom")

# print("My todo list:")
# for i in range(len(tasks)):
#     print(f"{i + 1}. {tasks[i]}")


# completed = tasks.pop(0)
# print(f"\nCompleted: {completed}")

# print("\nRemaining tasks:")
# for i in range(len(tasks)):
#     print(f'{i + 1}. {tasks[i]}')


# grades = {'Alice':95,'Bob':87,'Carol':92,'David':78}

# total=0
# for name in grades:
#     total = total + grades[name]

# average = total/len(grades)

# print("=== Grade Report ===")
# for name, score in grades.items():
#     print(f'{name}: {score}')

# print(f'\nClass Average: {average:.1f}')

# scores_list = list(grades.values())
# highest = max(scores_list)
# lowest = min(scores_list)

# print(f'Highest Grade: {highest}')
# print(f"Lowest Grade: {lowest}")


# contacts = {"Alice":"555-1234", "Bob":"555-5678",'Carol':"555-9012"}

# print("=== Contact Book ====")
# for name, phone in contacts.items():
#     print(f"{name}: {phone}")

# search_name = "Bob"

# if search_name in contacts:
#     print(f"\n {search_name}'s number: {contacts[search_name]}")
# else:
#     print(f'\n{search_name} not found')


# contacts['David'] = '555-3456'
# print(f'\nAdded David to Contacts')
# print(f'Total contacts: {len(contacts)}')

text = "the cat sat on the mat the cat was happy"
words = text.split()

word_counts={}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

print("Word Counts:")
for word, count in word_counts.items():
    print(f" '{word}' appears {count} time(s)")