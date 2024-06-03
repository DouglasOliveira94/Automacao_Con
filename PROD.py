#  horas gastas, 18 horas
#  feito por Douglas Oliveira
import pyautogui
import time
import re
import clipboard
from utils import perguntar_se_prossegue, informar_usuario
import sys

pyautogui.FAILSAFE = True
teste = 1
for _ in range(teste):
    if perguntar_se_prossegue('iniciando o Script'):
        time.sleep(3)
        pyautogui.click(x=67, y=108)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        text = clipboard.paste()
    # procura a frase desejada na linha
        nenhuma_tabela_disponivel = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        operacao_nao_permitida_nao_perturbe = re.search(
        r'Simulation=> Simulation=> Operação não permitida, cliente possui registro em Não Perturbe', text)
        saldo_desatualizado = re.search(
        r'Saldo desatualizado, favor consultar@@@@@ novamente no endpoint de Sa''l@@@do.', text)
        sem_saldo = re.search(r'Não foi encontrado nenhuma parcela com o valor maior que R\$ 10,00\.\.\.', text)
        cpf_invalido = re.search(
        r'CPF nao e valido', text)
        cliente_nao_autorizou_instituicao = re.search(
        r'O cliente não autorizou a instituição...', text)
        nao_pode_ser_maior_que = re.search(
        r'não pode ser maior que R', text)

        # entra na primeira linha se verificar o primeiro parametro
        if nenhuma_tabela_disponivel:
            nenhuma_tabela_disponivel = nenhuma_tabela_disponivel.group()
            print('---')
            pyautogui.click(x=67, y=108)
            pyautogui.click(x=67, y=108)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # pega o codigo da tabela para comparar e mudar
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(2)

            # pega o codigo da tabela para comparar e mudar
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(2)

            # pega o codigo da tabela para comparar e mudar
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(3)

            # pega o codigo da tabela para comparar e mudar
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(3)

            # pega o codigo da tabela para comparar e mudar
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(2)

            # pega o codigo da tabela para comparar e mudar
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=263)
                time.sleep(2)
        # Pega a outra frase
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=327)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            # copia para comparar se escreveu a mensagem certa
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # comparar para ver se esta certo
            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # Entrando em outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(x=146, y=329)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            # copiar para verificar se preencheu a mensagem corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # comparando para ver se escreveu certo
            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # entrando em outra mensagem
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=329)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            # comparando para ver se escreveu certo
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # comparando para ver se escreveu certo
            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # Entrando em outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=173, y=466)
        # Entrando em outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=134, y=329)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # comparando para ver se preencheu certo
            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # Entrando em outro erro
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=141, y=298)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            # Copiando para verificar se esta correto
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # comparando para verificar se esta certo
            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)

            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        print('Terminou a primeira linha')
    else:
        informar_usuario('Script Finalizado')
        sys.exit()
    # perguntando se quer iniciar outra linha
    if perguntar_se_prossegue('Deseja prosseguir para a proxima linha?'):
        time.sleep(2)
        pyautogui.click(x=67, y=124)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        text = clipboard.paste()
        segunda_linha = re.search(
            r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        if segunda_linha:
            segunda_linha = segunda_linha.group()
            print('---')
            pyautogui.click(x=67, y=124)
            pyautogui.click(x=67, y=124)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # verificando o codigo que esta na af
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=67, y=124)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=112, y=286)
                time.sleep(2)
            # verificando o codigo que esta na af
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=67, y=124)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=112, y=286)
                time.sleep(2)
            # verificando o codigo que esta na af
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=286)
                time.sleep(3)
            # verificando o codigo que esta na af
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=67, y=124)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=112, y=286)
                time.sleep(2)
            # verificando o codigo que esta na af
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=67, y=124)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=112, y=286)
                time.sleep(2)
            # verificando o codigo que esta na af
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=67, y=124)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(2)
                pyautogui.click(x=112, y=286)
                time.sleep(3)
        # verificando outra mensagem
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            pyautogui.click(145, 349)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verificando se preencheu corretamente
            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verificando outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(145, 349)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            # verificando se preencheu corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verificando se preencheu corretamente
            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verificando outra mensagem
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=349)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            # verificando se preencheu corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verificando outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(279, 495)
        # verificando outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(145, 349)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verificando se preencheu corretamente
            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verificando outra mensagem
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(145, 349)
            time.sleep(1)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            # verificando se preencheu corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        print('Terminou a segunda linha')
    else:
        informar_usuario("O usuário escolheu não prosseguir. Encerrando o script.")
        sys.exit()

    if perguntar_se_prossegue('Deseja prosseguir para a proxima linha?'):
        time.sleep(2)
        pyautogui.click(x=68, y=143)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        text = clipboard.paste()
        terceira_linha = re.search(
            r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        if terceira_linha:
            terceira_linha = terceira_linha.group()
            print('---')
            pyautogui.click(x=68, y=143)
            pyautogui.click(x=68, y=143)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # verifica codigo da tabela
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=143)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=118, y=303)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=143)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=118, y=303)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=253, y=303)
                time.sleep(3)
            # verifica codigo da tabela
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=143)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=118, y=303)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=143)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=118, y=303)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=143)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=118, y=303)
                time.sleep(2)
        # verifica outra mensagem
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=368)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(x=146, y=368)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra linha
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=368)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            # verifica se preencheu corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(180, 510)
        # verifica outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(139, 368)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(139, 368)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        print('Terminou a terceira linha')
    else:
        informar_usuario("O usuário escolheu não prosseguir. Encerrando o script.")
        sys.exit()

    if perguntar_se_prossegue('Deseja prosseguir? '):
        time.sleep(2)
        pyautogui.click(x=68, y=160)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        text = clipboard.paste()
        quarta_linha = re.search(
            r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        if quarta_linha:
            quarta_linha = quarta_linha.group()
            print('---')
            pyautogui.click(x=68, y=160)
            pyautogui.click(x=68, y=160)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # verifica codigo da tabela
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(3)
            # verifica codigo da tabela
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(2)
            # verifica codigo da tabela
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=117, y=321)
                time.sleep(2)
        # verifica outra mensagem
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            # clicar em pendente
            pyautogui.click(x=140, y=380)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=380)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            # verifica se preencheu corretamente
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            # clicar em pendente
            pyautogui.click(x=140, y=380)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            #  OP cadastrar manual
            pyautogui.click(171, 528)
        # verifica outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            # clicar em pendente
            pyautogui.click(x=140, y=380)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            # clicar em pendente
            pyautogui.click(x=140, y=380)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            # verifica se preencheu corretamente
            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        print('Terminou a quarta linha')

    else:
        informar_usuario("O usuário escolheu não prosseguir. Encerrando o script.")
        sys.exit()

    if perguntar_se_prossegue('Deseja Prosseguir?'):
        time.sleep(2)
        pyautogui.click(x=68, y=176)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        text = clipboard.paste()
        quinta_linha = re.search(
            r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        if quinta_linha:
            quinta_linha = quinta_linha.group()
            print('---')
            pyautogui.click(x=68, y=176)
            pyautogui.click(x=68, y=176)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # verifica codigo da af
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=176)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(2)
            # verifica codigo da af
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(2)
            # verifica codigo da af
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=202, y=107)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(3)
            # verifica codigo da af
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(2)
            # verifica codigo da af
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(2)
            # verifica codigo da af
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=160)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=335)
                time.sleep(2)
        # verifica outra mensagem
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            pyautogui.click(x=143, y=397)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        # verifica outra mensagem
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=397)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(x=143, y=397)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        # verifica outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=146, y=547)
        # verifica outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=139, y=397)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()
            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=142, y=397)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)

            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        print('Terminou a quinta linha')

    else:
        informar_usuario("O usuário escolheu não prosseguir. Encerrando o script.")
        sys.exit()

    if perguntar_se_prossegue('Deseja prosseguir? '):
        time.sleep(2)
        pyautogui.click(x=68, y=198)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        text = clipboard.paste()
        sexta_linha = re.search(
            r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...', text)
        if sexta_linha:
            sexta_linha = sexta_linha.group()
            print('---')
            pyautogui.click(x=68, y=198)
            pyautogui.click(x=68, y=198)
            time.sleep(3)
            pyautogui.click(x=260, y=391)
            pyautogui.click(x=260, y=391)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            tabela = clipboard.paste()
            tabela_int = int(tabela)
            # verifica codido da tabela
            if tabela_int == 1:
                time.sleep(1)
                pyautogui.write('11')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(2)
            # verifica codido da tabela
            elif tabela_int == 2:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(2)
            # verifica codido da tabela
            elif tabela_int == 4:
                time.sleep(1)
                pyautogui.write('12')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(3)
            # verifica codido da tabela
            elif tabela_int == 5:
                time.sleep(1)
                pyautogui.write('13')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(2)
            # verifica codido da tabela
            elif tabela_int == 11:
                time.sleep(1)
                pyautogui.write('1')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(2)
            # verifica codido da tabela
            elif tabela_int == 13:
                time.sleep(1)
                pyautogui.write('5')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(1)
                pyautogui.click(x=276, y=111)
                time.sleep(2)
                pyautogui.click(x=68, y=199)
                time.sleep(1)
                pyautogui.click(button='right')
                time.sleep(3)
                pyautogui.click(x=154, y=348)
                time.sleep(2)
        # verifica outra mensagem
        elif operacao_nao_permitida_nao_perturbe:
            pyautogui.click(button='right')
            pyautogui.click(x=145, y=411)
            time.sleep(3)
            nao_pertube = 'CLIENTE NO NAO PERTURBE'
            pyautogui.write(nao_pertube)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if nao_pertube == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif nao_pode_ser_maior_que:
            pyautogui.click(button='right')
            pyautogui.click(x=146, y=411)
            time.sleep(3)
            verificar_tabela = 'VERIFICAR TABELA'
            pyautogui.write(verificar_tabela)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if verificar_tabela == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cliente_nao_autorizou_instituicao:
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(x=145, y=411)
            time.sleep(3)
            sem_autorizacao = 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
            pyautogui.write(sem_autorizacao)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if sem_autorizacao == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif saldo_desatualizado:
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=146, y=547)
        # verifica outra mensagem
        elif sem_saldo:
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=139, y=411)
            time.sleep(2)
            sem_saldos = 'SEM SALDO'
            pyautogui.write(sem_saldos)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if sem_saldos == garantia:
                time.sleep(2)
                pyautogui.click(x=714, y=478)
            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()
        # verifica outra mensagem
        elif cpf_invalido:
            cpf_invalido = cpf_invalido.group()
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.click(x=142, y=411)
            dados_inconsistentes = 'DADOS DIVERGENTES'
            pyautogui.write(dados_inconsistentes)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            garantia = clipboard.paste()

            if dados_inconsistentes == garantia:
                time.sleep(2)
                pyautogui.press('enter')
                pyautogui.write(cpf_invalido)
                time.sleep(1)
                pyautogui.click(x=718, y=478)

            else:
                informar_usuario("Dados inconsistentes, Encerrando o script.")
                sys.exit()

        print('Terminou a sexta linha')
    else:
        informar_usuario("O usuário escolheu não prosseguir. Encerrando o script.")
        sys.exit()

    informar_usuario('Script Finalizado!')
