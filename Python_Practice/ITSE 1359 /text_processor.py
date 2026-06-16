def read_file(filename): # a function creation
    with open(filename, 'r') as file: #filename is opened and automatically closed with 'with' command. file is read with 'r'option
        text = (file.read())
        return(text)
    
def count_words(text):
    words = text.split()
    return(len(words))

def count_word_frequency(text):
    words = text.split()
    word_counts={}
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return(word_counts)

    # print("Word Counts:")
    # for word, count in word_counts.items():
    #     print(f" '{word}' appears {count} time(s)")

def find_longest_word(text):
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
    print(longest_word)
           
# def replace_word(text, old_word,new_word):
#     new_text=''
#     if old_word in text:
#         new_text = text.replace(old_word, new_word)

#     return(new_text)

# def find_numbers(text):
#     import re
#     pattern = r"\d+"
#     result = re.findall(pattern, text)
#     return(result)    
        
    

  

message = 'This is a test, to see if this is a good script'
# count_words(message)
# count_word_frequency(message)
find_longest_word(message)
# replace_word(message,'test','BAD')