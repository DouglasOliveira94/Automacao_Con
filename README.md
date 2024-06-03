# Automacao_Con_OP
Automação do setor de operações da concredito

# Automação de Sistema

Este script automatiza a interação com o sistema Agilus, realizando tarefas do NÃO DIGITADO --ERRO-- ROBÔ. Ele foi desenvolvido para reduzir o tempo manual necessário para essas tarefas repetitivas e aumentar a precisão.

## Requisitos

- Python 3.12
- Bibliotecas Python:
  - pyautogui
  - clipboard
  - re
  - tkinter
  - clipboard

- Sistema Operacional: Windows
- RAM: Pelo menos 4 GB
- Resolução da Tela: 1366x768 (recomendado para precisão do `pyautogui`)


Funções e Módulos
utils.py
perguntar_se_prossegue(mensagem)
Exibe uma caixa de diálogo perguntando ao usuário se deseja prosseguir.

Parâmetros:

mensagem (str): A mensagem a ser exibida na caixa de diálogo.
Retorna:
bool: True se o usuário clicar em "Sim", False se clicar em "Não".


informar_usuario(mensagem)
Exibe uma caixa de diálogo informando ao usuário uma mensagem.

Parâmetros:

mensagem (str): A mensagem a ser exibida na caixa de diálogo.
