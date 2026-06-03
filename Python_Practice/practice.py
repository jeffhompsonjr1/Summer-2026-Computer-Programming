file = open("welcome.txt", 'r')
all_lines = file.readlines()
print(f'Total lines: {len(all_lines)}')
for line in all_lines:
    print(line.strip())
file.close()