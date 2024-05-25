from customtkinter import *

linha_label_0 = 0
linha_label_1 = 1
linha_insert_text = 2
linha_label_resultado_0 = 3 # Escrita "Resultado:" 
linha_label_resultado = 4 # Mesma do erro
linha_buttons = 5

def erro(tipo):
    label_erro.grid(column=0, row=linha_label_resultado)
    if tipo == 1:
        text_erro.set("Valores inválidos.")
    else:
        text_erro.set("O espaço está vazio.")

def calcular(text):
    split = text.split()
    if verificar_valores(text, split):
        resultados = calcular_valores(split)
        exibir_valores(resultados)
    else:
        erro(1)

def limpar(text):
    label_erro.grid_remove()
    label_resultado_0.grid_remove()
    label_resultado.grid_remove()
    if text != "0":
        insertText.delete(0, "end")

def verificar_valores(text, split):
    if not text:
        return False
    elif type(text) != str:
        return False
    if len(split) < 2:
        return False
    else:
        for valor in split:
            if not valor.isdigit():
                return False
    return True

def lista_de_valores(valores):
    lista_de_valores = [int(valor) for valor in valores]
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

def calcular_valores(valores):
    resultados = {}
    resultados['lista'] = lista_de_valores(valores)
    resultados['total'] = valor_total(resultados['lista'])
    resultados['media'] = valor_media(resultados['total'], resultados['lista'])
    resultados['mediana'] = valor_mediana(resultados['lista'])
    resultados['variancia_amostral'] = valor_variancia_amostral(resultados['lista'], resultados['media'])
    resultados['coeficiente_variacao_porcentagem'] = valor_coeficiente_variacao_porcentagem(resultados['variancia_amostral'], resultados['media'])
    resultados['conjunto_homogeneo'] = is_conjunto_homogeneo(resultados['coeficiente_variacao_porcentagem'])
    return resultados

def exibir_valores(resultados):
    label_resultado_0.grid(column=0, row=linha_label_resultado_0, pady=(15,0))
    label_resultado.grid(column=0, row=linha_label_resultado, pady=(0,15))
    text_resultado_0.set("Resultados:")
    valor_media = resultados['media']
    text = f"O valor médio é: {valor_media}\n"
    valor_mediana = resultados['mediana']
    text += f"O valor mediano é: {valor_mediana}\n"
    valor_variancia_amostral = resultados['variancia_amostral']
    text += f"A variância amostral é: {valor_variancia_amostral}\n"
    valor_coeficiente_variacao_porcentagem = resultados['coeficiente_variacao_porcentagem']
    text += f"O coeficiente de variação é: {valor_coeficiente_variacao_porcentagem:.1f}%\n"
    conjunto_homogeneo = resultados['conjunto_homogeneo']
    text += f"O conjunto de valores é {'homogêneo' if conjunto_homogeneo else 'heterogêneo'}."
    text_resultado.set(text)

# Interface
janela = CTk()
janela.title("Estatística")
#janela.geometry("685x415")

# Texto 1
label_0 = CTkLabel(janela, text="Esse é um programa que calcula a média, mediana, variância amostral, coeficiente de variação e se um conjunto\nde valores é homogêneo ou heterogêneo.", text_color="#66B2FF")
label_0.grid(column=0, row=linha_label_0, padx=25, pady=(30, 30))
# Texto 2
label_1 = CTkLabel(janela, text="Digite os valores que deseja calcular (separados por espaço): ")
label_1.grid(column=0, row=linha_label_1)

# Entrada de texto
text = StringVar()
insertText = CTkEntry(janela, width=200, textvariable=text)
insertText.grid(column=0, row=linha_insert_text, pady=(10, 15))
text.trace("w", lambda *args: limpar("0"))

# Resultado
# Titulo
text_resultado_0 = StringVar()
label_resultado_0 = CTkLabel(janela, textvariable=text_resultado_0, text_color="#66B2FF")
# Resultado Completo
text_resultado = StringVar()
label_resultado = CTkLabel(janela, textvariable=text_resultado)
# Erro
text_erro = StringVar()
label_erro = CTkLabel(janela, textvariable=text_erro, text_color="red")

# Botões
frame = CTkFrame(janela)
frame.grid(column=0, row=linha_buttons, padx=10, pady=(15,30))
# Botão 1
button_1 = CTkButton(frame, text="Calcular", command=lambda: calcular(insertText.get()))
button_1.pack(side="left", padx=5, pady=10)
# Botão 2
button_2 = CTkButton(frame, text="Limpar", command=lambda: limpar(insertText.get()))
button_2.pack(side="right", padx=5, pady=10)

janela.mainloop()