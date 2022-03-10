"""takes in a list of words and a set of letters. Prints out words in the list that start with any letter in the set"""
word_list = ["hello", "hey", "goodbye", "yo", "yes"]
set_of_letters = {"h", "y"}

def print_upper_words(words, letter_set):
    for word in words:
        for letter in letter_set:
            if word.startswith(letter):
                print(word.upper())