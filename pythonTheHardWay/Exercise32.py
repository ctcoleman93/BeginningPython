#Learn Python the Hard Way
#Exersice 32: Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number
    
for fruit in fruits:
    print "A fruit of type: %s" % fruit

elements = []

for i in change:
    print "I got %r" % i

for i in range(0,6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Emlement was: %d" % i
    
practiceList = [[1,2,3,],[4,5,6]]
print practiceList
