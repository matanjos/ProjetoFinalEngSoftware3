### Funções em Python
   Em Python,uma função é uma sequência de comandos que executa uma tarefa quando é utilizada(chamada) no código. As funções possuem nomes e auxiliam o desenvolvedor a estruturar o seu código de formar organizada e intuitiva. Observe o exemplo abaixo de como declarar uma função:  
   
```python
def NOME( PARAMETROS ):
    COMANDOS  
```

   Utiliza-se a palavra reservada "def" antes do nome da sua função para especificar que trata-se de uma função. Em seguida e entre parênteses, nomeia-se os parâmetros que essa função receberá ao ser chamada, que serão os valores que o usuário(código) "envia" para a função ao chama-lá.  
   
  É possível atribuir qualquer nome para sua função, desde que este nome não seja uma palavra reservada e ela siga a regra de identificadores(caracteres) válidos.  
  
  A função exemplo a seguir imprime na tela a string(texto) pre definida, variando apenas uma parte do texto que é dependente do parâmetro(meu_nome) recebido :  
  
  ```python
def hello( meu_nome ):
      print('Ola',meu_nome)  
```
  
Para mais detalhes, o link abaixo contém exemplos e exceções sobre o uso de funções em Python :  
[Utilização de Funções em Python](https://panda.ime.usp.br/pensepy/static/pensepy/05-Funcoes/funcoes.html)
