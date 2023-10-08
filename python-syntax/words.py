def print_upper_words(words, start_chars={"e"}):
    """ Given a list of words, print only words beginning with the letters defined in start_chars. 
    All words are printed in upper case. The default filter letter is e """
    
    for word in words:
        word = word.casefold()
        for char in start_chars:
            char = char.casefold()
            if word.startswith(char):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "Howdy", "Eagle", "ears"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "Howdy", "Eagle", "ears"], {"h","g"})
