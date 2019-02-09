a = "Prashant"
print(a.find("ggggash"))
for i in range(len(a)):
	for j in range(i + 1):
		print(a[j:len(a) - i + j])
		print("a[" + str(j) + ":" + str(len(a) - i + j) + "]")
"abcef"
"cba"

"abcecba"
