#horas gastas, 9 horas
#feito por Douglas Oliveira
import pyautogui
import time
import re
import pyperclip
import clipboard
#loop para rodar quandas vezes desejar

pyautogui.FAILSAFE = True

rodagem = int(input('quantas vezes voce quer rodar? digite apenas numero: '))
time.sleep(3)
for _ in range (rodagem):
    time.sleep(3)
    pyautogui.click(x=67, y=108)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    #procura a frase desejada do erro
    nenhuma_tabela_disponivel = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    operacao_nao_permitida_nao_perturbe = re.search(
        r'[Simulation]=> [Simulation]=> Operação não permitida, cliente possui registro em Não Perturbe',text)

    esse_cpf_consultando_banco = re.search(
        r'Esse CPF já está sendo consultado no banco! Verifique novamente mais tarde...',text)
    
    fila_de_consulta = re.search(
        r'Você entrou na fila de consultas do banco! Aguarde até que sua consulta seja realizada..', text)
    
    saldo_desatualizado = re.search(
        r'Saldo desatualizado, favor consultar novamente no endpoint de Saldo.', text)
    
    sem_saldo = re.search(r'Não foi encontrado nenhuma parcela com o valor maior que R\$ 10,00\.\.\.', text)

    cpf_invalido = re.search(
        r'CPF nao e valido', text)
    
    cliente_nao_autorizou_instituicao = re.search(
        r'O cliente não autorizou a instituição...', text)
    
    nao_pode_ser_maior_que = re.search(
        r'não pode ser maior que R\$ [\d,.] e menor que R\$ [\d,.]+', text)
    
    #não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png',confidence=0.98 )

    #entra no if se achar o primeiro erro chamado primeira_linha
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
        #pega o codigo da tabela para comparar e mudar
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
            
        

        if tabela_int == 2:
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

        if tabela_int == 4:
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
        
        if tabela_int == 5:
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

        if tabela_int == 11:
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

        if tabela_int == 13:
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

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)


    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=173, y=466)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=134, y=328)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=141, y=298)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    
#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


#############################################################################

    print('Terminou a primeira linha')

    time.sleep(2)
    pyautogui.click(x=67, y=124)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(3)
    text = clipboard.paste()
    segunda_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
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
            pyautogui.click(x=112, y=286) #Mudar 
            time.sleep(2)
            

        if tabela_int == 2:
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

        if tabela_int == 4:
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
        
        if tabela_int == 5:
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

        if tabela_int == 11:
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

        if tabela_int == 13:
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

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(145,349)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(145,349)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass



    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(279,495)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(145,349)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(145,349)
        time.sleep(1)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    print('Terminou a segunda linha')


#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


###################################################################3

    time.sleep(2)
    pyautogui.click(x=68, y=143)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    terceira_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
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
            

        if tabela_int == 2:
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

        if tabela_int == 4:
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
        
        if tabela_int == 5:
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

        if tabela_int == 11:
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

        if tabela_int == 13:
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


#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)


    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)
        
#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(180,510)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(139,366)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(139,366)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

######################################################################3
    print('Terminou a terceira linha')


    time.sleep(2)
    pyautogui.click(x=68, y=160)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    quarta_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
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
            pyautogui.click(x=117, y=292)
            time.sleep(2)
            

        if tabela_int == 2:
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
            pyautogui.click(x=117, y=292)
            time.sleep(2)

        if tabela_int == 4:
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
            pyautogui.click(x=117, y=292)
            time.sleep(3)
        
        if tabela_int == 5:
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
            pyautogui.click(x=117, y=292)
            time.sleep(2)

        if tabela_int == 11:
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
            pyautogui.click(x=117, y=292)
            time.sleep(2)

        if tabela_int == 13:
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
            pyautogui.click(x=117, y=292)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        #clicar em pendente
        pyautogui.click(x=140, y=385)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)


    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        #clicar em pendente
        pyautogui.click(x=140, y=385)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        #OP cadastrar manual
        pyautogui.click(171,528)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        #clicar em pendente
        pyautogui.click(x=140, y=385)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)


    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        #clicar em pendente
        pyautogui.click(x=140, y=385)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
    
    print('Terminou a quarta linha')

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

##########################################################################

    time.sleep(2)
    pyautogui.click(x=68, y=176)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    quinta_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
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
            pyautogui.click(x=154, y=304)
            time.sleep(2)
            

        if tabela_int == 2:
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
            pyautogui.click(x=154, y=304)
            time.sleep(2)

        if tabela_int == 4:
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
            pyautogui.click(x=154, y=304)
            time.sleep(3)
        
        if tabela_int == 5:
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
            pyautogui.click(x=154, y=304)
            time.sleep(2)

        if tabela_int == 11:
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
            pyautogui.click(x=154, y=304)
            time.sleep(2)

        if tabela_int == 13:
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
            pyautogui.click(x=154, y=304)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=143, y=397)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=143, y=397)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=402)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)


#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=402)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    print('Terminou a quinta linha')

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

############################################################3


    time.sleep(2)
    pyautogui.click(x=68, y=198)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    sexta_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
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
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
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
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
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
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
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
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
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
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
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
            pyautogui.click(x=154, y=307)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass


    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)



#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass
    
    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    print('Terminou a sexta linha')

###########################################################################################

    time.sleep(2)
    pyautogui.click(x=68, y=217)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    setima_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if setima_linha:
        setima_linha = setima_linha.group()
        print('---')
        pyautogui.click(x=68, y=217)
        pyautogui.click(x=68, y=217)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=220)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
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
            pyautogui.click(x=154, y=338)
            time.sleep(2)

        if tabela_int == 4:
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
        
        if tabela_int == 5:
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
            pyautogui.click(x=154, y=338)
            time.sleep(2)

        if tabela_int == 11:
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
            pyautogui.click(x=154, y=338)
            time.sleep(2)

        if tabela_int == 13:
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
            pyautogui.click(x=154, y=338)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    print('Terminou a sétima linha')

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass
#############################################################3

    time.sleep(2)
    pyautogui.click(x=68, y=239)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    oitava_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if oitava_linha:
        oitava_linha = oitava_linha.group()
        print('---')
        pyautogui.click(x=68, y=239)
        pyautogui.click(x=68, y=239)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=239)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)


#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)

    print('Terminou a oitava linha')

    time.sleep(2)
    pyautogui.click(x=68, y=255)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    nona_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if nona_linha:
        nona_linha = nona_linha.group()
        print('---')
        pyautogui.click(x=68, y=255)
        pyautogui.click(x=68, y=255)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=255)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
        time.sleep(5)
    
    print('Terminou a nova Linha')

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass
    
    time.sleep(2)
    pyautogui.click(x=68, y=276)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    decima_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if decima_linha:
        decima_linha = decima_linha.group()
        print('---')
        pyautogui.click(x=68, y=276)
        pyautogui.click(x=68, y=276)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=276)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)


    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
        time.sleep(5)

    print('Terminou a décima linha')

    time.sleep(2)
    pyautogui.click(x=68, y=296)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    decima_primeira_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if decima_primeira_linha:
        decima_primeira_linha = decima_primeira_linha.group()
        print('---')
        pyautogui.click(x=68, y=296)
        pyautogui.click(x=68, y=296)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=296)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)



    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
        time.sleep(5)


    print('Terminou a 11ª linha')


    time.sleep(2)
    pyautogui.click(x=68, y=315)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    decima_segunda_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if decima_segunda_linha:
        decima_segunda_linha = decima_segunda_linha.group()
        print('---')
        pyautogui.click(x=68, y=315)
        pyautogui.click(x=68, y=315)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=315)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass
    
    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
        time.sleep(5)

    print('Terminou a 12ª linha')



    time.sleep(2)
    pyautogui.click(x=68, y=333)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(1)
    text = clipboard.paste()
    decima_terceira_linha = re.search(
        r'Não foi encontrado nenhuma tabela disponivel para esse CPF conforme as tabelas selecionadas...',text)
    if decima_terceira_linha:
        decima_terceira_linha = decima_terceira_linha.group()
        print('---')
        pyautogui.click(x=68, y=333)
        pyautogui.click(x=68, y=333)
        time.sleep(3)
        pyautogui.click(x=260, y=391)
        pyautogui.click(x=260, y=391)
        pyautogui.hotkey('ctrl', 'c') 
        time.sleep(2)
        tabela = clipboard.paste()
        tabela_int = int(tabela)
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
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)
            

        if tabela_int == 2:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 4:
            time.sleep(1)
            pyautogui.write('12')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(3)
        
        if tabela_int == 5:
            time.sleep(1)
            pyautogui.write('13')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 11:
            time.sleep(1)
            pyautogui.write('1')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)

        if tabela_int == 13:
            time.sleep(1)
            pyautogui.write('5')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(1)
            pyautogui.click(x=276, y=111)
            time.sleep(2)
            pyautogui.click(x=68, y=333)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(3)
            pyautogui.click(x=154, y=307)
            time.sleep(2)



    if operacao_nao_permitida_nao_perturbe:
        operacao_nao_permitida_nao_perturbe = operacao_nao_permitida_nao_perturbe.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        nao_pertube= 'CLIENTE NO NAO PERTURBE'
        pyautogui.write(nao_pertube) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cliente_nao_autorizou_instituicao:
        cliente_nao_autorizou_instituicao = cliente_nao_autorizou_instituicao.group()
        pyautogui.click(button='right')
        pyautogui.click(x=145, y=411)
        time.sleep(3)
        sem_autorizacao= 'SEM AUTORIZAÇÃO PARA REALIZAR A OPERAÇÃO'
        pyautogui.write(sem_autorizacao) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if saldo_desatualizado:
        saldo_desatualizado = saldo_desatualizado.group()
        pyautogui.click(button='right')
        time.sleep(3)
        pyautogui.click(x=146, y=547)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if nao_pode_ser_maior_que:
        nao_pode_ser_maior_que = nao_pode_ser_maior_que.group()
        pyautogui.click(button='right')
        pyautogui.click(x=146, y=327)
        time.sleep(3)
        verificar_tabela= 'VERIFICAR TABELA'
        pyautogui.write(verificar_tabela) 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=721, y=480)

    if sem_saldo:
        sem_saldo = sem_saldo.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=139, y=411)
        time.sleep(2)
        sem_saldo = 'SEM SALDO'
        pyautogui.write(sem_saldo)
        time.sleep(2)
        pyautogui.click(x=714, y=478)

#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.8)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass

    if cpf_invalido:
        cpf_invalido = cpf_invalido.group()
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(x=142, y=411)
        dados_inconsistentes='DADOS DIVERGENTES'
        pyautogui.write(dados_inconsistentes)
        pyautogui.press('enter')
        pyautogui.write(cpf_invalido)
        time.sleep(1)
        pyautogui.click(x=718, y=478)
        time.sleep(5)

    print('Terminou a 13ª linha')

    #ultima linha atualiza os dados, não mexa

    pyautogui.press('f3')
    time.sleep(4)
    pyautogui.click(834,71)
    time.sleep(60)


#codigo para tentar contornar caso o programa trave
    try:
        não_respondendo = pyautogui.locateOnScreen('nao_respondendo.png', confidence=0.6)
        if não_respondendo:
            time.sleep(120)
        else:
            pass
    except pyautogui.ImageNotFoundException:
        pass