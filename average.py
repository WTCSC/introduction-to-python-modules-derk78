import argparse 

import text_utils

def word_line(filename):
    #Start the count for the amount of lines at 0.
    count = 0 
    #Do the same for the amount of words in the file.
    amt_words = 0 
    #Open the text file to be read using the 'r' statement.
    file = open(filename, 'r') 
    #Use the readline() method to put each string in the text into an array.
    lines = file.readlines()  
    #Iterate through each line in the file. 
    for line in lines:  
        #For each new line in the file update count by 1.
        count = count + 1 
        #"amt_words" is the amount of words it's updated using our count_words function that 
        #we imported from our "text_utils" module to count the amount of words for each given string.
        amt_words = amt_words + text_utils.count_words(line)
    file.close() 
    #Caculate the average by dividing the amount of words by the amount of lines.
    count_avg = amt_words / count
    #Return the final average of words per line as an integer.
    return int(count_avg)

def main():
  parser = argparse.ArgumentParser(description='Average words per line in a file.')
  parser.add_argument('filename', help='The file to count lines from')
  args = parser.parse_args()

  avgwords = word_line(args.filename)
  print(f'Average words per line: {avgwords}')

if __name__ == '__main__': 
    main() 