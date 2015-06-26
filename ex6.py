# *-- coding: utf-8


# X 문장에 10 출력
x = "There are %d types of people" % 10
# Binary 에 "binary" 문자열 assign
binary = "binary"
#assign "don't" to do_not
do_not = "don't"
# print the below sentence with binry, do_not 
y = "Those who knows %s and thoes who %s." % (binary, do_not)


print x
print y

print "I said: %r" % x
print "I also said: '%s'" % y

hillarious = False
joke_evaluation = "Isn't taht joke so funny?! %r"

print joke_evaluation % hillarious

w = "This is the left side of ..."
e = "a string with a right side"

print w + e
