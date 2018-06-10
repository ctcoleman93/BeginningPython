#Learn Python the Hard Way
#Exersice 38: Doing things with lists

#variable ten_things is equal to the string statement
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print string statement to user
print "Wait there's not 10 things in that list, let's fix that."

#variable stuff is equal to ten_things turned to a list of strings
stuff = ten_things.split(' ')
#variable more_stuff is equal to the list of strings
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while the length of variable stuff is not equal to 10....
while len(stuff) != 10:
    #variable next_one is equal to the first stirng in the list more_stuff
    next_one = more_stuff.pop()
    #print what variable was "popped" from the list to the user
    print "Adding: ", next_one
    #add the variable next_one to the list stuff
    stuff.append(next_one)
    #print the length of list stuff to user
    print "There's %d items now." % len(stuff)
    #return to the top of loop and continue until length of list stuff is equal to 10

#print the list stuff to the user
print "There we go: ", stuff

#print statement to user
print "Let's do some things with stuff."

#print the second item in the list stuff
print stuff[1]
#print the last item in the list stuff
print stuff[-1]
#grab last item from list stuff and display to user
print stuff.pop()
#combine list stuff itno one print statement and print to user
print ' '.join(stuff)
#join the fourth and fifth item in the list stuff, combine them to one print statement and add # before each print
print '#'.join(stuff[3:5])

