#Learn Python the Hard Way
#Exersice 18: Names, Variables, Code, Functions

#function like the argv scripts
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#make that shorter
def print_two_again(arg1, arg2):
    print "arg2: %r, arg2: %r" % (arg1, arg2)

#function takes an argument
def print_one(arg1):
    print "arg1: %r" % arg1

#function takes NO argument
def print_none():
    print "I got nothin"

print_two("Chris","Coleman")
print_two_again("Chris","Coleman")
print_one("First!")
print_none()
