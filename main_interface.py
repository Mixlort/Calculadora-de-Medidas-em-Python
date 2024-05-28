from customtkinter import *

linha_label_0 = 0
linha_label_1 = 1
linha_insert_text = 2
linha_label_resultado_0 = 3
linha_label_resultado = 4
linha_buttons = 5


def Calcular(text):
    split = text.split()
    if VerificarValores(text, split):
        resultados = CalcularValores(split)
        ExibirValores(resultados)
    else:
        label_erro.grid(column=0, row=linha_label_resultado)
        text_erro.set("Valores inválidos.")


def Limpar(text):
    label_erro.grid_remove()
    label_resultado_0.grid_remove()
    label_resultado.grid_remove()
    if text != "0":
        insertText.delete(0, "end")


def VerificarValores(text, split):
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


def ListaDeValores(valores):
    ListaDeValores = [int(valor) for valor in valores]
    return ListaDeValores


def ValorTotal(ListaDeValores):
    ValorTotal = sum(ListaDeValores)
    return ValorTotal


def ValorMedia(ValorTotal, ListaDeValores):
    ValorMedia = ValorTotal / len(ListaDeValores)
    return ValorMedia


def ValorMediana(ListaDeValores):
    ValorMediana = (
        sorted(ListaDeValores)[len(ListaDeValores) // 2]
        if len(ListaDeValores) % 2 != 0
        else (
            sorted(ListaDeValores)[len(ListaDeValores) // 2]
            + sorted(ListaDeValores)[len(ListaDeValores) // 2 - 1]
        )
        / 2
    )
    return ValorMediana


def ValorVarianciaAmostral(ListaDeValores, ValorMedia):
    ValorVarianciaAmostral = sum(
        [(valor - ValorMedia) ** 2 for valor in ListaDeValores]
    ) / (len(ListaDeValores) - 1)
    return ValorVarianciaAmostral


def ValorCoeficienteVariacaoPorcento(ValorVarianciaAmostral, ValorMedia):
    ValorCoeficienteVariacaoPorcento = (ValorVarianciaAmostral**0.5) / ValorMedia * 100
    return ValorCoeficienteVariacaoPorcento


def ConjuntoHomogeneo(ValorCoeficienteVariacaoPorcento):
    conjunto_homogeneo = ValorCoeficienteVariacaoPorcento < 30
    return conjunto_homogeneo


def CalcularValores(valores):
    resultados = {}
    resultados["lista"] = ListaDeValores(valores)
    resultados["total"] = ValorTotal(resultados["lista"])
    resultados["media"] = ValorMedia(resultados["total"], resultados["lista"])
    resultados["mediana"] = ValorMediana(resultados["lista"])
    resultados["variancia_amostral"] = ValorVarianciaAmostral(
        resultados["lista"], resultados["media"]
    )
    resultados["coeficiente_variacao_porcentagem"] = ValorCoeficienteVariacaoPorcento(
        resultados["variancia_amostral"], resultados["media"]
    )
    resultados["conjunto_homogeneo"] = ConjuntoHomogeneo(
        resultados["coeficiente_variacao_porcentagem"]
    )
    return resultados


def ExibirValores(resultados):
    label_resultado_0.grid(column=0, row=linha_label_resultado_0, pady=(15, 0))
    label_resultado.grid(column=0, row=linha_label_resultado, pady=(0, 15))
    text_resultado_0.set("Resultados:")
    ValorMedia = resultados["media"]
    text = f"O valor médio é: {ValorMedia}\n"
    ValorMediana = resultados["mediana"]
    text += f"O valor mediano é: {ValorMediana}\n"
    ValorVarianciaAmostral = resultados["variancia_amostral"]
    text += f"A variância amostral é: {ValorVarianciaAmostral}\n"
    ValorCoeficienteVariacaoPorcento = resultados["coeficiente_variacao_porcentagem"]
    text += f"O coeficiente de variação é: {ValorCoeficienteVariacaoPorcento:.1f}%\n"
    conjunto_homogeneo = resultados["conjunto_homogeneo"]
    text += f"O conjunto de valores é {'homogêneo' if conjunto_homogeneo else 'heterogêneo'}."
    text_resultado.set(text)


janela = CTk()
janela.title("Estatística")

label_0 = CTkLabel(
    janela,
    text="Esse é um programa que calcula a média, mediana, variância amostral, coeficiente de variação e se um conjunto\nde valores é homogêneo ou heterogêneo.",
    text_color="#66B2FF",
)
label_0.grid(column=0, row=linha_label_0, padx=25, pady=(30, 30))
label_1 = CTkLabel(
    janela, text="Digite os valores que deseja calcular (separados por espaço): "
)
label_1.grid(column=0, row=linha_label_1)

text = StringVar()
insertText = CTkEntry(janela, width=200, textvariable=text)
insertText.grid(column=0, row=linha_insert_text, pady=(10, 15))
text.trace("w", lambda *args: Limpar("0"))

text_resultado_0 = StringVar()
label_resultado_0 = CTkLabel(
    janela, textvariable=text_resultado_0, text_color="#66B2FF"
)
text_resultado = StringVar()
label_resultado = CTkLabel(janela, textvariable=text_resultado)
text_erro = StringVar()
label_erro = CTkLabel(janela, textvariable=text_erro, text_color="red")

frame = CTkFrame(janela)
frame.grid(column=0, row=linha_buttons, padx=10, pady=(15, 30))
button_1 = CTkButton(frame, text="Calcular", command=lambda: Calcular(insertText.get()))
button_1.pack(side="left", padx=5, pady=10)
button_2 = CTkButton(frame, text="Limpar", command=lambda: Limpar(insertText.get()))
button_2.pack(side="right", padx=5, pady=10)

janela.mainloop()
