### Variáveis em Python

	Em Python, não existe um comando para declarar uma variável. Basta atribuir um nome e um valor a ela, tal como no exemplo abaixo:  
```python
VarNum  = 5  
VarNome = "Nome_de_Alguém"  
```
 Como exposto acima, para atribuir um valor númerico basta inseri-lo diretamente e para adicionar um "texto"(que no exemplo seria o nome de alguém), basta colocar o texto entre aspas simples ou duplas(' '  ou "  " ).  
Recomenda-se a escolha do nome da variável de tal forma que seja bastante clara a intenção do seu uso para facilitar o entedimento do seu algoritmo. Além disso, Python é uma linguagem "Case Sensitive", que significa dizer que o "Python" diferencia letras maiúsculas de minúsculas. Ou seja, uma variável chamada 'a' e outra chamada 'A' são variáveis diferentes.  

	Em Linguagens tipadas as variáveis são declaradas com o tipo de dado já determinado. Em python isso não acontence, podemos atribuir à uma mesma variável qualquer valor de qualquer tipo de dado quantas vezes quisermos.

```
varNum = 2        #atribui um inteiro a uma variável
print(2)          #imprime um inteiro

varNum = "Olá mundo!"     #atribui uma string à mesma variável
print(varNum)             #imprime uma string

varNum = [1, 2, 3]        #atribui um vetor de inteiros à mesma variável
print(varNum)             #imprime o vetor
``` 
	O tempo de vida de uma variável e onde ela é acessível depende do local que ela é declarada. A parte do programa que uma variável é acessível é chamada de escopo e a duração para a qual a variável existe de seu tempo de vida. As variáveis podem ter escopo local e escopo global.
####Escopo local

	Um variável declarada dentro de uma função tem escopo local. Isso significa que ela só existe quando a função é chamada e ao término da função ela é destruída, não sendo possível acessá-la em outras parte do programa. Toda vez que a função é chamada é criada uma nova variável. Essa variável também é acessível a outros módulos nos quais importe o módulo que ela foi definida. Uma utilidade das variávels globais é armazenar valores constantes para serem acessados por funções.

	Deve-se ter muito cuidade ao manipular variáveis globais, pois se for atribuído um valor para uma variável global dentro de função, na verdade se estará criando é uma variável local com o mesmo nome.

####Escopo global

	Uma variável com escopo global é declara fora das funções e pode ser acessada em todos os módulos onde ela é definida.
Para mais detalhes, o link abaixo contém exemplos e exceções sobre o uso de variáveis em Python :  
[Utilização de Variáveis em Python](https://www.explorandoti.com.br/o-que-sao-variaveis-e-como-funcionam-no-python-3/)  
