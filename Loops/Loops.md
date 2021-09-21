### Loops em Python

#### Comando for  
O comando for em Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência diferente do que costuma ser em C ( que permite ao usuário definir o passo de iteração e a condição de parada ou Pascal ( que sempre itera sobre uma progressão aritmética de números). Por exemplo, o código abaixo exibe os elementos da lista em ordem.  
```python  
List_alunos = ['Joao', 'Maria', 'Jose']
for name in List_alunos:
  print(name)  
```  

Para iterar sobre sequências numéricas, é possível usar a função range() que gera uma progressão aritmética sendo que o ponto de parada fornecido nunca é incluído na lista. Por exemplo, o código abaixo exibe os número de 0 a 9.
```python  
for i in range(10):
  print(i)  
```  
É possível iniciar o intervalo com outro número, ou alterar a razão da progressão (inclusive com passo negativo).  

#### Comando while  

O laço de repetição while executa enquanto a condição permanece verdadeira. Em Python, como em C, qualquer valor inteiro que não seja zero é considerado verdadeiro enquanto o zero é considerado falso. A condição pode também ser uma cadeia de caracteres ou uma lista, ou qualquer sequência sendo que qualquer coisa com um tamanho maior que zero é verdadeiro, enquanto sequências vazias são falsas. Os operadores padrões de comparação são os mesmos de C: < (menor que), > (maior que), == (igual), <= (menor ou igual), >= (maior ou igual) e != (diferente). Por exemplo, o código abaixo exibe os números de 1 a 10.  
```python  
a = 0
while a < 10:  
  a = a + 1  
  print(a)   
```  
Abaixo temos o Exemplo do funcionamento do while:

![while e if e else](https://github.com/matanjos/ProjetoFinalEngSoftware3/blob/main/Controle%20de%20fluxo/while%20if%20else.jpg)

Para mais exemplos, acesse: [Exemplos de Códigos](https://github.com/matanjos/ProjetoFinalEngSoftware3/tree/main/c%C3%B3digos)
