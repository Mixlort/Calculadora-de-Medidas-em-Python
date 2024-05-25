import os
import msvcrt
from tkinter import *

def exibir_nome_do_programa():
    print("""
 #######             ##                ##       ##                ##       ##
  ##   #             ##                ##                         ##
  ## #     #####    #####    ####     #####    ###      #####    #####    ###      ####     ####
  ####    ##         ##         ##     ##       ##     ##         ##       ##     ##  ##       ##
  ## #     #####     ##      #####     ##       ##      #####     ##       ##     ##        #####
  ##   #       ##    ## ##  ##  ##     ## ##    ##          ##    ## ##    ##     ##  ##   ##  ##
 #######  ######      ###    #####      ###    ####    ######      ###    ####     ####     #####
    """)
    print("Esse é um programa que calcula a média, mediana, variância amostral, coeficiente de variação e se um conjunto de valores é homogêneo ou heterogêneo.\n")

def erro():
    print("\nValores inválidos. Pressione qualquer tecla para tentar novamente...")
    msvcrt.getch()
    os.system("cls")
    main()

def definir_valores():
    valores = input("Escolha os valores que deseja calcular (separados por espaço): ")
    split = valores.split()
    if not valores:
        erro()
    elif type(valores) != str:
        erro()
    elif len(split) < 2:
        erro()
    for valor in split:
        if not valor.isdigit():
            erro()
    return valores

def lista_de_valores(valores):
    lista_de_valores = [int(valor) for valor in valores.split()]
    return lista_de_valores

def valor_total(lista_de_valores):
    valor_total = sum(lista_de_valores)
    return valor_total

def valor_media(valor_total, lista_de_valores):
    valor_media = valor_total / len(lista_de_valores)
    return valor_media

def valor_mediana(lista_de_valores):
    valor_mediana = sorted(lista_de_valores)[len(lista_de_valores) // 2] if len(lista_de_valores) % 2 != 0 else (sorted(lista_de_valores)[len(lista_de_valores) // 2] + sorted(lista_de_valores)[len(lista_de_valores) // 2 - 1]) / 2
    return valor_mediana

def valor_variancia_amostral(lista_de_valores, valor_media):
    valor_variancia_amostral = sum([(valor - valor_media) ** 2 for valor in lista_de_valores]) / (len(lista_de_valores) - 1)
    return valor_variancia_amostral

def valor_coeficiente_variacao_porcentagem(valor_variancia_amostral, valor_media):
    valor_coeficiente_variacao_porcentagem = (valor_variancia_amostral ** 0.5) / valor_media * 100
    return valor_coeficiente_variacao_porcentagem

def is_conjunto_homogeneo(valor_coeficiente_variacao_porcentagem):
    conjunto_homogeneo = valor_coeficiente_variacao_porcentagem < 30
    return conjunto_homogeneo

def is_conjunto_heterogeneo(valor_coeficiente_variacao_porcentagem):
    conjunto_heterogeneo = valor_coeficiente_variacao_porcentagem >= 30
    return conjunto_heterogeneo

def calcular_valores(valores):
    resultados = {}
    resultados['lista'] = lista_de_valores(valores)
    resultados['total'] = valor_total(resultados['lista'])
    resultados['media'] = valor_media(resultados['total'], resultados['lista'])
    resultados['mediana'] = valor_mediana(resultados['lista'])
    resultados['variancia_amostral'] = valor_variancia_amostral(resultados['lista'], resultados['media'])
    resultados['coeficiente_variacao_porcentagem'] = valor_coeficiente_variacao_porcentagem(resultados['variancia_amostral'], resultados['media'])
    resultados['conjunto_homogeneo'] = is_conjunto_homogeneo(resultados['coeficiente_variacao_porcentagem'])
    resultados['conjunto_heterogeneo'] = is_conjunto_heterogeneo(resultados['coeficiente_variacao_porcentagem'])
    return resultados

def exibir_valores(resultados):
    valor_media = resultados['media']
    print(f"O valor médio é: {valor_media}")
    valor_mediana = resultados['mediana']
    print(f"O valor mediano é: {valor_mediana}")
    valor_variancia_amostral = resultados['variancia_amostral']
    print(f"A variância amostral é: {valor_variancia_amostral}")
    valor_coeficiente_variacao_porcentagem = resultados['coeficiente_variacao_porcentagem']
    print(f"O coeficiente de variação é: {valor_coeficiente_variacao_porcentagem:.1f}%")
    conjunto_homogeneo = resultados['conjunto_homogeneo']
    print(f"O conjunto de valores é {'homogêneo' if conjunto_homogeneo else 'heterogêneo'}.\n")

def finalizar_app():
    print('Pressione "1" para rodar o programa novamente, ou qualquer outra tecla para fechar.')
    tecla = msvcrt.getch().decode('utf-8')
    if tecla == '1':
        os.system("cls")
        main()
    else:
        exit()

def main():
    exibir_nome_do_programa()
    valores = definir_valores()
    resultados = calcular_valores(valores)
    exibir_valores(resultados)
    finalizar_app()

main()