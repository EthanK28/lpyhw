cars = 100 # Set cars to 100, assign a value to cars
space_in_a_car = 4.0 # Set space in a car to 4.0
drivers = 30 # set drivers to 30
passengers = 90 # set passengers to 90
cars_not_driven = cars - drivers #
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There aer only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
print "Hey %s there" % "30"
