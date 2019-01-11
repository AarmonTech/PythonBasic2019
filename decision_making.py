#Any decision making needs a block of code,
#if this then that block of code should run,
#In c or any other langauage, block of code is mostly presented as :
"""
 if (some condition ){
	statement1
	statement2
  }
else{
	statement3,
	statemenet4
 }

"""
#but in python, any block of code is written with indentation
#indentation is when you start your line of code with some spaces
# so our if in python is as folows:

a, b  = int( input( "Enter a : ") ) , int( input( "Enter b : " ) ) # this is another way of taking input in one line


if a > b:
	print("a is greater than b,")
	print("b is smaller than a,")
else:
	print("a is smaller than b,")
	print("b is greater than a,")

#yet another way to write above is

if (a > b):
	print("a is greater")
else:
	print("b is greater")


##################################
#else if ==>> elif
##################################

#in python, else if of c or java is presented as elif

if condition1:
	print("Condition 1 satisfied")
elif condition2:
	print("2 satisfied")
elif condition3:
	print("3 satisfied")
elif condition4:
	print("4 satisfied")
else:
	print("Non of above conidtion satisfied")
