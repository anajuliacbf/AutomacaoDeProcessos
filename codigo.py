import pyautogui
import time
import pandas

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui -> fazer automações com python
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

# Passo 2: Fazer login
time.sleep(3) # Espera 3s para a aplicação carregar
pyautogui.click(x=612, y=510)
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhasuperdificil")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=602, y=365)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)