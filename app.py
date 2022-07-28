from tkinter import *
from tkinter import Tk, ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
import json

# cores
branco = "#fafafa"
preto = "#171717"
azul = "#110069"

janela = Tk()
janela.title("Tracker Coin")
janela.configure(bg=preto)
janela.attributes("-alpha", 0.98)
janela.geometry("350x400")
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_cima = Frame(janela, width=350, height=80, bg=branco, relief=SOLID)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=350, height=320, bg=preto, relief=SOLID)
frame_baixo.grid(row=1, column=0)

# Função monitorar bitcoin


def monitorar():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL%2CGBP"

    response = requests.get(api_link)
    dados = response.json()

    valor_dolar = float(dados['USD'])
    valor_dolar_formatado = "${:,.3f}".format(valor_dolar)
    label_bitcoin['text'] = valor_dolar_formatado

    valor_euro = float(dados['EUR'])
    valor_euro_formatado = "€{:,.3f}".format(valor_euro)
    label_showeuro['text'] = valor_euro_formatado

    valor_gbp = float(dados['GBP'])
    valor_gbp_formatado = "£{:,.3f}".format(valor_gbp)
    label_showlibra['text'] = valor_gbp_formatado

    valor_real = float(dados['BRL'])
    valor_real_formatado = "R${:,.3f}".format(valor_real)
    label_showreal['text'] = valor_real_formatado

    frame_baixo.after(1000, monitorar)


# Frame cima
img = Image.open('icon.png')
img = img.resize((50, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_icon = Label(frame_cima, image=img, bg=branco)
app_icon.place(x=40, y=10)

title_label = Label(frame_cima, text="Tracker Coin",
                    font="Raleway 20 bold", bg=branco, fg=preto)
title_label.place(x=100, y=18)

# Frame baixo

label_bitagora = Label(frame_baixo, text="Bitcoin agora:",
                       font="Raleway 9 italic", bg=preto, fg=branco)
label_bitagora.place(x=135, y=20)

label_bitcoin = Label(frame_baixo, text="",
                      font="Raleway 24 bold", bg=preto, fg=branco)
label_bitcoin.place(x=80, y=42)

label_euro = Label(frame_baixo, text="Conversão Euros:",
                   font="Raleway 12 ", bg=preto, fg=branco)
label_euro.place(x=20, y=120)
label_showeuro = Label(frame_baixo, text="R$100",
                       font="Raleway 12 bold ", bg=preto, fg=branco)
label_showeuro.place(x=160, y=120)

label_libra = Label(frame_baixo, text="Conversão Libras Esterlinas:",
                    font="Raleway 12 ", bg=preto, fg=branco)
label_libra.place(x=20, y=170)
label_showlibra = Label(frame_baixo, text="R$100",
                        font="Raleway 12 bold ", bg=preto, fg=branco)
label_showlibra.place(x=240, y=170)


label_real = Label(frame_baixo, text="Conversão Reais:",
                   font="Raleway 12 ", bg=preto, fg=branco)
label_real.place(x=20, y=220)
label_showreal = Label(frame_baixo, text="R$100",
                       font="Raleway 12 bold ", bg=preto, fg=branco)
label_showreal.place(x=160, y=220)

monitorar()

janela.mainloop()
