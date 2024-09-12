def count_chars(text):
    #Set the variable characters to the length of the text since the amount of characters is the total length of the text.
    characters = len(text)
    #Then we return the total length of the text.
    return characters 

def count_words(text):
    #Start the count at 0.
    count = 0
    #We do the .split() on our text to get the individual words from the string, and iterate through them using a for loop.
    for word in text.split():
    #For each word increase our variable "count" by one.
        count = count + 1
    #return the final count.
    return count

def count_sentences(text):
    #Using our other function count_chars to determine the amount of characters in the given text if it has zero values return zero.
    if count_chars(text) == 0:
        return(0)
    #In the below lines we use the count() method to count each time punctuation shows up in the text and count it as a sentence.
    period = text.count('.')
    exclamation = text.count('!')
    question = text.count('?')
    #Use a variable to be the last character in a given string.
    lastchar = text[-1]
    #If the last character isn't any of the following punctuation we add one if it does have punctuation then our variable "addone" is left at 0.
    if lastchar not in ['!', '.', '?']:
        addone = 1 
    else:
        addone = 0
    #Finally add together all of the punctuation we counted as well as the "addone" variable for any sentences that don't end with punctuation.
    return(period + exclamation + question + addone)
    