# Assignment 2

"""

4. Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

Comment your code to explain what is happening in each logical step. 

"""

def high_score_word(input_string): # define a function to take input as an argument
    values = { # creat a json with <key> as alphabets and <value> as its score
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
}
    
     # assign the json value to values json
    word_score = [] # create an empty word_value list
    list_of_words = input_string.split() # store the input string in term of list of words
    print(list_of_words) # print the words list
    for word in list_of_words: # looping over list_of_words and itterate over each word
        score = score_of_word(word,values) # vall schore_of_word function to get the score of each word
        word_score.append(score) # append the score to the word_score list
    max_score = max(word_score) # using mx function get the maximum score in the word_score list
    index_no = word_score.index(max_score) # get the index number of the max_score
    print('highest scoring word is : '+list_of_words[index_no]) # print the highest scoring word from the sentence to the console

def score_of_word(word,values): # define the score_of_word function that takes word and values json as input parameters
    value = 0 # initialise value to 0
    for char in word: # looping on the word and itterating on each character 'char'
        value = value + values[char] # add value of the character to value variable and store in value
    return value # return value which will have score of the word

high_score_word(input('Enter the string (containing only alphabets , in smaller case)to check : ')) # call high_score_word method and as the user to enter the string in console