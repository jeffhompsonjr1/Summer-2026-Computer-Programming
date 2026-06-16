'''Practice Activity 1: File Statistics Counter
File name: file_stats.py

Objective: Create a script that reads a text file and calculates basic statistics.

Instructions:

Create a function count_lines(filename) that:
Opens and reads a text file
Returns the total number of lines
Create a function count_words(filename) that:
Reads the file content
Splits the content into words
Returns the total word count
Create a function count_characters(filename) that:
Returns the total number of characters (excluding spaces)
Create a function save_stats(stats, output_filename) that:
Writes all statistics to an output file
Create a sample text file called sample.txt with this content:
Python is a great programming language.

It is easy to learn and fun to use.

Many developers love Python.'''

# This is a empty list to add function output values 
stats=[]

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        newlines = [x for x in lines if x != '\n']
        return(len(newlines))

stats.append(count_lines('sample.txt')) # 


def count_words(filename): # Function to count word
    with open(filename, 'r') as file:
        content = file.read()
        return(len(content.split()))
    

stats.append(count_words('sample.txt'))

def count_characters(filename): # Function to count characters
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        characters = ''.join(words)
        return(len(characters))

stats.append(count_characters('sample.txt'))

def save_stats(stats,output_filename): # Function to add stats
    with open(output_filename,'a') as file:
        file.write(f"File Statistics for: sample.txt\n\n")
        file.write('='*20)
        file.write(f"\nTotal lines: {stats[0]}\n")
        file.write(f'\nTotal words: {stats[1]}\n')
        file.write(f'\nTotal characters: {stats[2]}\n')
        file.write(f"\nStatistics saved to: {output_filename}")
        return(output_filename)

save_stats(stats,'stats_output.txt')# Input the stats list into the function and outputs the stats_output.



       










        
        