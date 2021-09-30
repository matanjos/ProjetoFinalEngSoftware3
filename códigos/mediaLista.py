  lista = [ 5.5, 2, 7, 9, 8.9] #cria uma lista contendo as notas de 5 estudantes
  
  
  def maiorNotaTurma(lista):    #define uma função para calcular a maior nota da turma
    maiorNota = 0
    for nota in lista:
       if nota > maiorNota:
          maiorNota = nota
    return maiorNota
   
  def calcMediaTurma(lista):  #define uma função para calcular a media da turma
    mediaDaTurma = sum(lista)/len(lista) #calcula a media dos elementos da lista  e salva numa variável chamada media
    return mediaDaTurma
  
  maiorNota = maiorNotaTurma(lista)
  media = mediaDaTurma(lista)
  
  print(maiorNota) #exibe o valor contido na variavel maiorNota
  print(media) #exibe o valor contido na variavel media
  
