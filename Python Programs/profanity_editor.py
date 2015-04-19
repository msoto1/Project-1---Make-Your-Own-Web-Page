import urllib

def read_text():    #function to read text from a file
    quotes = open("C:\Users\Marco\Desktop\Intro to Programming\Project 1 - Make Your Own Web Page\Python Programs\movie_quotes.txt") #opens file
    contents_of_file = quotes.read()    #read text file
    print(contents_of_file)     #prints text file
    quotes.close()  # closes file that was opened
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse word!")
    else:
        print("Could not scan the document properly.")

read_text()  #calls function
