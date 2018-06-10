#Learn Python the Hard Way
#Exersice 24: More Practice

#print to the user what where about to do
print "Let's practice everything."
#\' in order to print the '
#\\ in order to print the \
#\n in order to print a new line
#\t in order to print a tabbed line
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

#Set the variable poem to the text of the poem
#""" allows exactly what we type to printed new lines and all
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
not comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------------------"
#print the value of the variable poem
print poem
print "-------------------------------"

#set the variable five to an equation that is equal to 5
five = 10 - 2 + 3 - 6
#text edditor %s to print the string of the variable five
print "This should be five: %s" % five

#define the function secret_formula with the variable started
def secret_formula(started):
    #variable jelly_beans is equal to the equation variable started multiplied 500 times
    jelly_beans = started * 500
    #variable jars is equal to the equation variable jelly_beans divided by 1000
    jars = jelly_beans / 1000
    #variable crates is equal to the variable jars divided by 100
    crates = jars / 100
    #the function will return the 3 variables
    return jelly_beans, jars, crates
#variable start_point is equal to 10000    
start_point = 10000
#variables beans, jars, and crates are equal to the return of the function secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)
#print the variable start_point in the string at %d as a decimal int
print "With a starting point of: %d" % start_point
#print the funtion return
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way: "
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


