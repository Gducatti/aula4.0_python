#Funções
#Serve pra organizar o código e para reaproveitamento
#Primo pobre do microserviço

#Sintaxe
#def nome_funcao(parametros separados por virgula):
#   instruções
#   return expressão

#1o passo é a definição da função
#2o passo é o uso

print('Funções')
print('Função simples')

#1o passo
def OlaMundo ():
    print('Ola Mundo')

#2o passo
OlaMundo()

#Função com parametros
#A gente define o parametro apenas dizendo o seu nome
#Não precisamos definir o tipo do parametro
print('\nFunção com parametro e uso posicional')
def Soma (p1, p2):
    total = p1 + p2
    print (total)

print('O total é: ', end=' ')
Soma(5, 6)

print('\nFunção com parametro e uso nomeado')
def Subtracao(p1, p2):
    total = p1 - p2
    print(total)
print('Posicional')
print('O total é: ', end=' ')
Subtracao(5, 6)

print('Nomeado')
print('O total é: ', end=' ')
Subtracao(p2=8, p1=5)

#Escopo
#No python e em qualquer linguagem há uma discussão sobre escopo
#O escopo é a VISIBILIDADE da variavel
#Existem variaveis de ESCOPO GLOBAL e VARIAVEIS de ESCOPO LOCAL
#No escopo GLOBAL as variaveis são definidas no programa principal
clima = 'inverno' #O clima é de escopo global
def MostraClima():
#Percebemos que mesmo dentro da função conseguimos acessar o
#valor da variavel clima
    print(f'O clima de hoje é de {clima}')

MostraClima()

#A unica regra é que a variavel global não pode estar definida
#depois da função

#E se nós tivessemos uma variavel que fosse definida dentro da função?
#Ou seja escopo local
#Será que conseguiriamos ver o valor dela no programa principal

def MostraTemperatura():
    temperatura = 13
    print(f'A temperatura hoje é de {temperatura} graus')

MostraTemperatura()

def DefineTemperatura():
    #A variavel aqui tem escopo local
    #Ou seja, não conseguimos acessar seu valor
    #no programa principal
    temp = 14
#Isso não funciona
#DefineTemperatura()
#print(f'A temperatura é de {temp}')

print('\nRetorno da Função')

def Soma2 (p1, p2):
    total = p1 + p2
    return total

#O def permite que usemos direto em outras funções
n1 = 8
n2 = 9
print(f'A soma de {n1} e {n2} é {Soma2(n1, n2)}')

def Saudacao (nome):
    return 'Bom Dia' + nome + ' !'

print(Saudacao('Anakin'))