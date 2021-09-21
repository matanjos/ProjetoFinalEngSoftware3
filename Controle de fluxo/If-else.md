### If-else em Python
  
  A capacidade de controlar seu fluxo baseada em certas condições é essencial para qualquer programa e uma das maneiras que o programador tem de criar esse controle é através dos recursos de controle da linguagem. A maneiras mais comum de realizar esse controle é através das condicionais if,elif e else.  
  Essas condicionais são palavras chaves(reservadas) do Python utilizadas para indicar uma execução condicional no algoritmo,permitindo selecionar quais blocos de códigos serão executados e quais não serão a depender das condições existentes. O fluxograma em alto nível funciona da seguinte forma:  
  A condição definida é verdadeira? Se sim, execute o bloco de código abaixo. Se não, não execute o bloco de código abaixo e execute a alternativa predefinida,caso exista.  
    
  Observe os exemplos a seguir :
  ```python
Python_Case_Sensitive = True  
  
if Python_Case_Sensitive == True:  
	print("Python é case sensitive.")
else:
	print("Python não é case sensitive.")
```
  
Observação : Não é necessário fazer "if Python_Case_Sensitive == True" , para digitar menos, escreva apenas "if Python_case_Sensitive".  
Observação 2: O comando "If" verifica se a condição definida é verdadeira ou falso. Portanto, é possível fazer,por exemplo :  
  ```python
VarCondicao = "Texto"  
if VarCondicao == "Texto":  
	print("Python é case sensitive.")
else:
	print("Python não é case sensitive.")
```    
De forma similar, além de uma string, é possível comparar valores ou até mesmo variáveis diretamente.  

  Para mais informações, acesse o link abaixo :  
  [Fluxo de Controle em Python](https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/)
