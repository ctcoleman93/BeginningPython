#Learn Python the Hard Way
#Exersice 15: Reading Files

# From module sys import the arguement function
from sys import argv
 
# Arguments to be brought into program
script, filename = argv

#open file given in argument when variable txt is called
txt = open(filename)

#display file name to user
print "Here's your file %r: " % filename
#display contents of filename
print txt.read()

#ask user to type name of file again
print "Type the filename again:"
#get filename from user
file_again = raw_input("-->")

#open file using raw_input to get filename
txt_again = open(file_again)

#print contents of file
print txt_again.read()

