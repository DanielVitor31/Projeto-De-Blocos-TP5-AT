from utils.menu_generico import exibir_menu
from constantes.constantes import CONSOLE_REDUZIDO
from negocio_tp3.negocio_crud import *


def menu_exibir_tp3():
    """Menu do TP3 - Joins entre dados de clientes/funcionários."""

    opcoes = {
        1: ("Left Join (dicionário)",
            lambda: left_join_dicionario(CONSOLE_REDUZIDO)),
        2: ("Right Join (dicionário)",
            lambda: right_join_dicionario(CONSOLE_REDUZIDO)),
        3: ("Inner Join (dicionário)",
            lambda: inner_join_dicionario(CONSOLE_REDUZIDO)),
        4: ("Left Join (lista)",
            lambda: left_join_lista(CONSOLE_REDUZIDO)),
        5: ("Right Join (lista)",
            lambda: right_join_lista(CONSOLE_REDUZIDO)),
        6: ("Inner Join (lista)",
            lambda: inner_join_lista(CONSOLE_REDUZIDO)),
    }

    exibir_menu(
        "MENU TP3 - JOINS",
        opcoes,
        texto_sair="Voltar para o Menu Principal",
    )
    print("Você voltou para o Menu Principal.")
