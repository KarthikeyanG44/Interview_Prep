def factorial_recursion(num):
	if num == 0:
		return 1
	elif num == 1:
		return num
	else:
		return num * factorial_recursion(num-1)



num = 4
print(factorial_recursion(num))