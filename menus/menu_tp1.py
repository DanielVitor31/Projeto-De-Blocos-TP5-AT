from utils.menu_generico import exibir_menu
from constantes.constantes import CONSOLE_REDUZIDO
from tarefas_tp1.tarefas import *


def menu_exibir_tp1():
    """Menu do TP1 - Compras de peças. (Tarefas)"""
    
    # Usei "lambda" para evitar o problema de chamar a função antes do menu
    opcoes = {
        1: ("Exibir todas as compras",
            lambda: compras_exibir(CONSOLE_REDUZIDO)),
        2: ("Exibir uma compra específica",
            lambda: compra_exibir(CONSOLE_REDUZIDO)),
        3: ("Adicionar nova compra",
            lambda: compras_adicionar(CONSOLE_REDUZIDO)),
        4: ("Atualizar status de uma compra",
            lambda: compras_status_atualizar(CONSOLE_REDUZIDO)),
    }

    exibir_menu(
        "MENU TP1 - COMPRAS",
        opcoes,
        texto_sair="Voltar para o Menu Principal",
    )
    print("Você voltou para o Menu Principal.")
