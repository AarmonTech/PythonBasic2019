"""a = {"roll":4,"prashant":"tiwari","att":8}

for i in a.items():
	print(i[1])

for i in a.keys():
	print(i, " : ", a[i])
"""

li = [1,2,1,4,6,9,8,9,6,5,9,3,2,2,4,5,6,7,5,8,2,3,6,3,2,5,3,4,6,5,4,7,5,6,8]
a = {}

for i in li:
	if i in a:
		a[i] = a[i] + 1
	else:
		a[i] = 1

print(a)
