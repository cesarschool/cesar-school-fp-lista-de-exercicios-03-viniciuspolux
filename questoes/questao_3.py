## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

loc1 = 0
loc2 = 0
loc3 = 0
loc4 = 0

def main():

    def robot(x):
        global loc1
        global loc2
        global loc3
        global loc4
        x = x.split()
        if x[0] == 'CIMA':
            loc1 += int(x[1])
        if x[0] == 'BAIXO':
            loc2 += int(x[1])
        if x[0] == 'ESQUERDA':
            loc3 += int(x[1])
        if x[0] == 'DIREITA':
            loc4 += int(x[1])

    while True:
        x = input('Tuplas: ').upper()
        if x == '':
            break
        else:
            robot(x)
            continue

    locF = ((loc1 - loc2) ** 2 + (loc3 - loc4) ** 2) ** (1 / 2)
    locF = round(locF)
    print('Distancia percorrida: ', locF)

    
if __name__ == '__main__':
    main()
