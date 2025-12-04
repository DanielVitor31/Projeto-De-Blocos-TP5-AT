from utils.menu_generico import exibir_menu
from json_tp4.json_crud_db import inserir_atualizar, deletar_clientes


def menu_exibir_tp4():
    """Menu do TP4 - Clientes em JSON."""

    opcoes = {
        1: ("Inserir e atualizar clientes", inserir_atualizar),
        2: ("Deletar clientes", deletar_clientes),
    }

    exibir_menu(
        "MENU TP4 - CLIENTES (JSON)",
        opcoes,
        texto_sair="Voltar para o Menu Principal",
    )
    print("Você voltou para o Menu Principal.")
