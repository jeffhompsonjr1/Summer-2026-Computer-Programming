#Text Formatter

formatted_text=[] # Empty lists to update formats
title_text=[] # Empty lists to update title format
def clean_text(text): # Removes leading and trailing whitespaces and returns a clean text
    with open(text, 'r') as file: # Opens text input file
        print(f"\nReading: {text}\n\nOriginal lines\n")
        for line in file.readlines():#Loops each line of the file as lists
            if line != '\n':# checks for blank lines
                formatted_text.append(line.strip()) # appends stripped line to
                print(f'"{line.strip()}"\n') #prints each line with content 
    return(formatted_text)

def format_title(text): # Converts text to title case and returns formatted text
    print("Formatted lines:\n")
    for line in text:
        print(f'"{line.title()}"','\n')
        title_text.append(line.title())
    global new_text
    new_text = '\n'.join(title_text)
    return(new_text) 

def replace_words(text,old_word,new_word):# Replaces words as needed.
    text = text.replace(old_word,new_word)    
    return(text)

def process_file(input_file,output_file): # Reads input file, applies all formatting functions, writes the result to output file.
     with open (output_file, 'w') as file:
        print("Text Formatter\n\n",'='*10)             
        clean_text(input_file)
        format_title(formatted_text)
        file.write(new_text)
        print(f'Saved to:\n{output_file}')
       
# clean_text('messy_text.txt')
# format_title(formatted_text)
# replace_words(new_text,'Test','Success')

process_file('messy_text.txt','clean_text.txt')
