# boot em analise
import time
import clipboard
import re
import webbrowser
import pyautogui
from datetime import datetime
pyautogui.FAILSAFE = True
hoje = datetime.today().strftime('%d/%m/%Y')
num_vezes = int(input('quantas vezes voce quer rodar? digite apenas numero: '))

for i in range(num_vezes):
    # Texto da frase
    pyautogui.click(x=67, y=108)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    text = clipboard.paste()
    url = 'www.google.com.br'
    # Verificar se "API" está na frase
    if "API" in text:
        # Expressão regular para encontrar números
        regex = r'\d+'

        # Encontrar todos os números na frase
        numeros = re.findall(regex, text)

        # Salvar os números em uma variável (lista de strings)
        numeros_encontrados = [num for num in numeros]

        # Juntar os três primeiros índices em uma string
        CPF = ''.join(numeros_encontrados[:4])
        # abrir a url do banco
        webbrowser.open(url)
        time.sleep(7)

        # arrumando a data

        pyautogui.click(835, 299)
        pyautogui.write(hoje)
        time.sleep(1)
        pyautogui.click(1075, 299)
        pyautogui.write(hoje)
        time.sleep(1)
        # colocando o CPF
        pyautogui.click(594, 375)
        pyautogui.write(CPF)
        time.sleep(1)
        # clicando para filtrar
        pyautogui.click(907, 453)
        time.sleep(2)
        # clicando para entrar no cadastro
        pyautogui.click(1267, 571)
        # arrastando a barra
        time.sleep(2)
        pyautogui.moveTo(1358, 178)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(1358, 668, duration=2)
        pyautogui.mouseUp(button='left')
        # clicando para abrir o fgts
        pyautogui.click(382, 602)
        # arrastando mais a barra
        time.sleep(1)
        pyautogui.moveTo(1358, 480)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(1358, 707, duration=2)
        pyautogui.mouseUp(button='left')
        time.sleep(1)
        try:
            cef = pyautogui.locateOnScreen('nao corresponde ao CEF.png', confidence=0.85)
            if cef:
                time.sleep(1)
                # voltando ao sistema
                pyautogui.click(221, 750)
                time.sleep(1)
                # preenchendo os dados
                pyautogui.click(x=67, y=108)
                pyautogui.click(button='right')
                time.sleep(1)
                pyautogui.click(126, 404)
                time.sleep(3)
                pyautogui.write('SEM SALDO PARA REALIZAR A OPERAÇÃO')
                time.sleep(1)
                pyautogui.click(714, 481)
                time.sleep(1)
                # atualizando as tabelas
                pyautogui.press('f3')
                time.sleep(4)
                pyautogui.click(834, 71)
                time.sleep(30)



            else:

                # voltando ao sistema
                pyautogui.click(221, 750)
                time.sleep(1)
                # se nao ocorrer atualizar as tabelas
                pyautogui.press('f3')
                time.sleep(4)
                pyautogui.click(834, 71)
                time.sleep(20)
        except pyautogui.ImageNotFoundException:
            pass
    pyautogui.press('f3')
    time.sleep(4)
    pyautogui.click(834, 71)
    time.sleep(20)

i + 1


