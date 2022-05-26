# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    read_file_content("./story.txt", "r")
    return "Hello World"
    #ffsd



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}
    #tgj
text = open("./story.txt", "r") 

  
# Create an empty dictionary 

d = dict() 

  
# Loop for each line of the file 

for line in text: 

    line = line.strip() 

    line = line.lower() 

  

    # Split the line into words 

    words = line.split(" ") 

    for word in words: 

        # Check if the word is already in dictionary 

        if word in d: 

            # Increase count of word by +1 

            d[word] = d[word] + 1

        else: 

            d[word] = 1

  
# Print the dictionary 

for key in list(d.keys()): 

    print(key, ":", d[key])