def n_th_fibonacci_number(n):
	if n <= 1:
		return n
	else:
		return n_th_fibonacci_number(n-1)+n_th_fibonacci_number(n-2)


n_th_term = 10

print(n_th_fibonacci_number(n_th_term))