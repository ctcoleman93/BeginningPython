#Learn Python the Hard Way
#Exersice 6: Strings and Text

# variable x is equal to a string with and integer format character
x = "There are %d types of people." % 10
# variable binary is equal to the string 'binary'
binary = 'binary'
# variable do_not is equal to string 'don't'
do_not = "don't"
# variable y is equal to a string with two format characgters
y = "Those who know %s and those who %s." % (binary, do_not)

# the value of variable x is displayed to the user
print x
# the value of the variable y is display to the user
print y

# variable x is used as a format character and its value is displayed within the string and displayed to the user
print "I said %r." % x
# variable y is used as a format character and its value is displayed within the string and display to the user
print "I also said: %s." % y

# variable hilarious is equal to the boolean expression False
hilarious = False
# variable joke_evealueaion is equal to a string with a unassigned format character
joke_evaluation = "Isn't that joke so funny?! %r"

# varaible joke_evaluation is displayed with variable hilarious insterted into the string as a format character
print joke_evaluation % hilarious

# variable w is asigned to a string
w = "This is the left side of ..... "
# variable e is asigned to a string
e = "a string with a right side."

#variables w and e are displayed to the user
print w + e

