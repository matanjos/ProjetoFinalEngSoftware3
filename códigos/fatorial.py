def fatorial (n): 				#Definição da função FATORIAL recebendo um valor "n" para ser calculado.
	if n==1: 				#Critério de parada.
		return 1			#
	else:					#Recursividade.
		return (n*fatorial(n-1))	
