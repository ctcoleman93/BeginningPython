#Learn Python the Hard Way
#Exersice 35: Branches and Functions

#from the sys module import the function exit
#the exit function allows the user to exit program based on a condition
from sys import exit

#define function gold_room
def gold_room():
    print "This room is full of gold. How much do you take?"
    
    #variable next is equal to the users imput
    next = raw_input(">")
    #if user entry has a 1 or a 0 then...
    if "0" in next or "1" in next:
        #variable how_much is equal to user input as an integer
        how_much = int(next)
    #otherwise run dead function with statement
    else:
        dead("Man, learn to type a number.")
    #if how_much is less than 50 then...   
    if how_much < 50:
        #print to user and exit program
        print "Nice, you're not greedy, you win!"
        exit(0)
    #otherwise run dead function with statemnt
    else:
        dead("You greedy bastard!")

#define function bear_room       
def bear_room():
    #print room info to user and ask for prompt
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    #bear_moved is False
    bear_moved = False
    
    #while True pretty much just means run this group of if elif statements
    while True:
        #get input from user
        next = raw_input(">")
        
        #if user enters take honey
        if next == "take honey":
            #go to dead function with the string statement
            dead("The bear looks at you then slaps your face off.")
        #if user enters taunt bear and bear_moved is false
        elif next == "taunt bear" and not bear_moved:
            #print to user they may go through the door
            print "The bear has moved from the door. You can go through it now."
            #set bear_moved to True
            bear_moved = True
        #if user enters taunt bear and bear_moved is True
        elif next == "taunt bear" and bear_moved:
            #go to dead function with string statement
            dead("The bear gets pissed off and chews your leg off.")
        #if user enters open door and bear_moved is True
        elif next == "open door" and bear_moved:
            #go to fucntion gold_room()
            gold_room()
        #Otherwise....
        else:
            #print to user we don't understand statement
            print "I got no idea what that means."
#define the cthulhu_room function            
def cthulhu_room():
    #print to user useful info about the room
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever startes at you and you go insane."
    print "Do you flee for you life or eat your head?"
    
    #prompt user for input and set input to the variable next
    next = raw_input(">")
    
    #if user enters flee
    if "flee" in next:
        #go to function start() and run
        start()
    #if user enters head
    elif "head" in next:
        #kill user and run dead function
        dead("Well that was tasty!")
    #anything else restart cthulhu_room
    else:
        cthulhu_room()

#define the dead function with string statements set to variable why        
def dead(why):
    #print variable why + good job
    print why, "Good job!"
    #close program
    exit(0)

#define the start() function    
def start():
    #print useful info to the user
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    #prompt user for input and set it to the variable next
    next = raw_input(">")
    
    #if user enters left
    if next == "left":
        #run bear_room() function 
        bear_room()
    #if user enters right
    elif next == "right":
        #run cthulhu_room() function
        cthulhu_room()
    #otherwise run dead funciton
    else:
        dead("You stumble around the room until you starve.")

#run start() function        
start()

            
 
