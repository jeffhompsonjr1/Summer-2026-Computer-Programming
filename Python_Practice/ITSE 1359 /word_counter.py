#Practice Activity 5: Word Frequency Counter
#Create a program that counts how often each word appears in a text file.

print("\nWord Frequency Counter\n\n","="*40,'\n')

def read_file(filename): # Reads and returns the file contents
    print(f"\nAnalyzing: {filename}\n")
    with open (filename, 'r') as file:
        global words # creates a global variable outside of function
        words = file.read() # creates variable from the read file
        return(words)


def count_words(text): # 
    global count_dict #creates global dictionary outside of definition
    count_dict={} #creates empty dictionary
    lower_case = text.lower() # Converts text to lowercase using lower()
    split_words = lower_case.split() #Splits text into words using split()
    for i in split_words:
        i = i.strip(".") # strips the period from each words.
        if i not in count_dict: # Using the dictionary to count each word
            count_dict[i] = 1 
        else:
            count_dict[i] += 1

    return(count_dict)

def find_most_common(word_counts):
    most_common_count = 1 # a counter and empty string to capture the word and count value
    most_common_word =''

    for k,v in word_counts.items(): #Finds and returns the most frequent word
        if v > most_common_count:
            most_common_count = v
            most_common_word = k
    print(f'Most common word:\n"{most_common_word}" ({most_common_count}times)')
    print(f'\nTotal unique words: {len(word_counts.keys())}')

def display_results(word_counts): #Prints each word and its count
    print("Word Counts:\n")
    for name, count in word_counts.items():
        print(f'{name}: {count}\n')
    
        
    
read_file('story.txt')
count_words(words)
display_results(count_dict)
find_most_common(count_dict)


