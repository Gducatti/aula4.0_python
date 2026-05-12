def MostrarNota():
    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media < 6:
        print('Você foi Reprovado!')
    else:
        print('Você foi Aprovado!')

MostrarNota()