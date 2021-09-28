def fib(n):		#Definição da Funçõa de Fibonacci
	if n==0:	#Critério de parada da função de Fibonacci
		return 0
	elif n==1:	#Critério de parada da função de Fibonacci
		return 1
	else:		#Recursividade.
		return (fib(n-1)+fib(n-2))
