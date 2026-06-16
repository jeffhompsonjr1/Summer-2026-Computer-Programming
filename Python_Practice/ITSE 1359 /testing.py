def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        newlines = [x for x in lines if x != '\n']
        return(len(newlines))

def count_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        return(len(words))

def count_characters(filename):
    with open(filename, 'r') as file:
        words = (file.read().split())
        merge = ''.join(words)
        return(len(merge))
    
lines =print(f'\nTotal lines: {count_lines('sample.txt')}\n')
words=print(f'\nTotal Words: {count_words('sample.txt')}\n')
characters=print(f'\nTotal Characters: {count_characters('sample.txt')}\n')
    
stats = [lines,words,characters]

def save_stats(stats, output_filename):
    with open(output_filename, 'w') as file:
        file.write("File Statistics for: sample.txt\n")
        file.write("="*40)
        for x in stats:
            file.write(x)

        

save_stats(stats,'stats_output.txt')
