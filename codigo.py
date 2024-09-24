# passo a passo do projeto de automaçao 
# 1 passo: abrir o navegador e entrar no site
# 2 passo: fazer o login na pagina
# 3 passo: importar os dados
# 4 passo: cadastrar os produtos
# 5 passo: repetir os produtos

import pyautogui as gui
import time
import pandas as pd

gui.PAUSE = 0.3

gui.press("win")
gui.write("chrome")
gui.press("enter")
gui.click(x=862, y=629)

gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
gui.press("enter")
time.sleep(3)

gui.click(x=685, y=451)
gui.write("pythonimpressionador@gmail.com")
gui.press("tab")
gui.write("sua senha")
gui.click(x=955, y=638)
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    gui.click(x=653, y=294)
    codigo = tabela.loc[linha, "codigo"]
    gui.write(str(codigo))
    gui.press("tab")
    gui.write(str(tabela.loc[linha, "marca"]))
    gui.press("tab")
    gui.write(str(tabela.loc[linha, "tipo"]))
    gui.press("tab")
    gui.write(str(tabela.loc[linha, "categoria"]))
    gui.press("tab")
    gui.write(str(tabela.loc[linha, "preco_unitario"]))
    gui.press("tab")
    gui.write(str(tabela.loc[linha, "custo"]))
    gui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        gui.write(str(tabela.loc[linha, "obs"]))
    gui.press("tab")
    gui.press("enter")
    gui.scroll(5000)