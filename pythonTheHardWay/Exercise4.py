#Learn Python the Hard Way
#Exersice 4: Variables and Names

#there are 100 cars
cars = 100
#there is room for 4 people
space_in_car = 4.0
#there are 30 drivers total
drivers = 30
#there are 90 passengers total
passengers = 90
#cars without drivers is found by subtracting available cars and drivers
cars_not_driven = cars - drivers
#cars with drivers is equal to the amount of drivers
cars_driven = drivers
#capacity is found by multiplyting cars driven and the space in each car
carpool_capacity = cars_driven * space_in_car
#average amount of passengers in each car is found by dividing passengers and cars driven
average_passengers_per_car = passengers / cars_driven

#print the results to the user
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
