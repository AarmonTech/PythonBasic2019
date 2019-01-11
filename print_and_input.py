#########################
#Print
#########################

#in python 3 print function is just a print()
# which takes argumenst , which needs to be printed

print("Hello World")

print("Another Hello World", 1, 2, 3, 4, 5)

a = "This is a String, so it has to be in double quotes."
b = 'Python supports single quotes, too, so this is in a single quotes.'

#if we want to print above, along side, we can do that in single print()

print(a, b)

#print function always prints a \n when it has done, printing, 
#to avoid that, we can do something, like this

print("Hello",end="")
print("World")

#i would suggest you to try to put another things as end="oooo", and see what output it brings

############################
#Input
############################
 
#In python3, input is mere a function input()
#which may, or may not take a string as an arguments
# that string would be a prompt, to print for asking user for the input

a = input("Enter value of a : ")
b = input("Enter value of b : ")

c = a + b
#now try to print c and check what your result is, 
# you would see that it just concataneted the number,instead of adding,
#This happened, because python 3 takes input in form of a string, 
# if we want to take integer orfloat value, we have to cast or convert it to int / float
# As told in class, for current purpose, we can just do


a = int(a)
b = int(b)

c = a + b
print(c)  

#if you go further with python, you will get to learn many more ways to do things, 
#like you can do the above things in single line like :
print( int( input( "Enter value of a :  ") ) + int( input( "Enter value of b : " ) ) )
#above is same as before

############################
#Points to remember
############################

#understand the difference:
#print("Hello") vs print(Hello) #this will error of hello not defined

