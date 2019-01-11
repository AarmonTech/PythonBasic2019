#####################################
#Two kinds of For loop we would be using,
#####################################
# a for loop in most language look likes : 
"""
for (i = 0; i < 20; i++){
	cout>>i;
}

"""
#python does it as this:
for i in range(20):
	print(i)

for i in range(20,100,5):# starts from 20, ends at 99( one before 100,) and takes 5 steps, skipping 4 values each times
	print(i)

######################################
#Little special thing in python
#Python as did a very good job, when we want
#to implement a for loop in any list, string, array
#or any other kind of object, in which we can increment
######################################

#let's take a string first
name = "Prashant"

#below for loop holds the value of each character in name "Prashant" on the varibale 'l'
#and loops untill the character in "Prashant" are finished
#This is an easy way to incremenet in any string
#For each character in name, each loop will hold  that character in a variable of for(here 'l'): 


for l in name:
	print(l)

#Now lets see a bit complex for loop,
#if you try to make this with c / c++ loop,
#you would know how beautifully python has made programming

#this is a list, which holds another list of different sizes, and that holds strings of different sizes
students = [ ["pra","sha","nt"], ["ti","wari","shivay"], ["namah","hjh"], ["wgek"] ]

#this will print, all 4 lists, try to understand the elements
for s in students:
	print (s)

########
##Nested loop
########
#here we would try to print each, letters in some way
#try to understand, what we are trying to do here

for l in students:
	for t in l:
		for r in t:
			print(r,end="-")
		print("\n_______")
	print(" Inner List Ends")
print ("Outer List Ends")

#another example
students = [ ["prashant","mango","Elex"], ["sagar","grapes","cs"], ["divyam","mango","ec"] ]


for l in students:
    print ( l[0] + " Likes " + l[1] + " And is in " + l[2] + " Branch")



#for loop to take five inputs from the user
students = []
for i in range(5): #this is same as for(i=0,i<=5,i++){} in c
	s = input("enter str:")
	students.append(s)
print ( students )



"""
#Take input, until nothing is entered,
l = []
a = ""

while True:
	a = input("Enter name to enter into list : ")
	if( a == ""):
		break
	l.append(a)

print(l)
"""
