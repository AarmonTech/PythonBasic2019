#list is a collection of data type enumerated by index startinng from 0
#unlike in c / c++, python supports lists with any kinds of data type

#with uniform data type
l = [1,2,3,4,5,6,7,8,9]
print(l)

#with different, data type
l = [1,2,3,4.5,"d",7,"prashant"]
print(l)


#list can have a list inside of it,
l = [34, "prashant", 56.78, 45, ["tiwari", 79], 56]

students = ["prashant", "tiwari", "sagar", "mohit", "saurav", "gaurav", "manish", "manoj"]
print ( l[-2][1])

print "..................................."

#slicing in lists, goes same as in strings
print(students[2:6])

#stepping in lists, goes same as in strings
print(students[2:6:2])

#negetive indexing, goes same as in strings
print(students[-3])

#note that negetive indexing starts from -1, not -0, coz there aint no thing as -0

#printing 3rd last name's 3rd character
print(students[-3][4])
