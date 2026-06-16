# text_processor.py
# Module 3 Mastery Assessment
# Jeff Thompson
# 12 June 2026

import re  # Import for regular expressions

def read_file(filename):
    """Read and return the contents of a text file."""
    with open(filename, 'r') as file: #filename is opened and automatically closed with 'with' command. file is read with 'r'option
        text = (file.read())
        return(text)
    pass

def count_words(text):
    """Count and return the total number of words in the text."""
    words = text.split()
    return(len(words))
    pass

def count_word_frequency(text):
    """Count how many times each word appears. Return a dictionary."""
    words = text.split()
    word_counts={}
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return(word_counts)
    pass

def find_longest_word(text):
    """Find and return the longest word in the text."""
    words = list(text.split())
    word_length= 0
    word_group={}
    longest_word=''
    for word in words:
           word_group[word] = len(word)
    for word, length in word_group.items():
        if length > word_length:
            word_length = length
            longest_word = word
    return(longest_word)
    pass

def replace_word(text, old_word, new_word):
    """Replace old_word with new_word in the text."""
    new_text=''
    if old_word in text:
        new_text = text.replace(old_word, new_word)
    
    return(new_text)

    pass

def find_numbers(text):
    """Use regex to find all numbers in the text. Return a list."""
    numbers = re.findall(r"\d+", text)
    return(numbers)    
    pass

def save_results(filename, word_count, longest_word, word_frequencies, numbers_found):
    """Save the analysis results to a file."""
    with open(filename, 'w') as file:
        file.writelines("="*20)
        file.writelines('\nTEXT FILE PROCESSOR\n')
        file.writelines("="*20)
        file.write(f'\nReading file: {filename}\n')
        file.write("\nFile loaded successfully!\n")
        file.write('\n---Analysis Results ---\n')
        file.write(f'\nTotal words: {word_count}\n')
        file.write(f'\nLongest Word: {longest_word}\n')
        file.write('\n---Numbers Found (using regex)---\n')
        file.write(f'\n{numbers_found}\n')
        file.write(f'\nTotal Numbers found: {len(numbers_found)}\n')
        file.write('\n---Word Frequency---\n')
        file.write(f'\n{word_frequencies}\n')
        file.write(f'\n{replace_word(filename,'Python','Java')}\n')
    pass

# Main program
print("================================")
print("TEXT FILE PROCESSOR")
print("================================")

# Step 1: Read the file
text = read_file("input.txt")
print("Reading file: input.txt")
print("File loaded successfully!")

# Step 2: Count words
total_words = count_words(text)
print(f"\n--- Analysis Results ---")
print(f"Total words: {total_words}")

# Step 3: Find longest word
longest = find_longest_word(text)
print(f"Longest word: {longest}")

# Step 4: Find numbers using regex
numbers = find_numbers(text)
print(f"\n--- Numbers Found (using regex) ---")
print(numbers)
print(f"Total numbers found: {len(numbers)}")

# Step 5: Count word frequency
frequencies = count_word_frequency(text)
print("\n--- Word Frequency ---")
for word, count in frequencies.items():
    print(f"{word}: {count}")

# Step 6: Replace a word
new_text = replace_word(text, "Python", "Java")
print(f'\n--- Text Replacement ---')
print(f'Replaced "Python" with "Java"')

# Step 7: Save results
save_results("output.txt", total_words, longest, frequencies, numbers)
print("\nResults saved to: output.txt")