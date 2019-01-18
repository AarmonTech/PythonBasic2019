class Im_num:


	def __init__(self,real, img):
		self.r = real
		self.i = img

	def __str__(self):
		return str(self.r) + " + i" + str(self.i) 

	def __add__(self, another):
		sum_r = self.r + another.r
		sum_i = self.i + another.i
		
		return Im_num(sum_r,sum_i)

	def __sub__(self, another):
		sum_r = self.r + another.r
		sum_i = self.i + another.i
		
		return Im_num(sum_r,sum_i)
		

a = Im_num(10,20)
b = Im_num(8,9)


c = a - b

print(a + b)
print(b + a)
