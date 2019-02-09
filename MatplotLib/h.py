li = [1,2,3,4,2,6,4,3,3,9,4,5,7,8,8]
b = {}
for i in li:
	if i in b:
		b[i] = b[i]+1
	else:
		b[i] = 1
print(b)
