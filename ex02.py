def LadosPoligono():
    lados = int(input('Insira o numero lados do poligono: '))
    if lados == 3:
        print('TRIÂNGULO')
    elif lados == 4:
        print('QUADRILATERO')
    elif lados == 5:
        print('PENTAGONO')
    else:
        print('VALOR INVALIDO')
LadosPoligono()