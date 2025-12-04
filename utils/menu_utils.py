import os
import platform

def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def menu_validar_entrada(opcao_escolhida, opcao_limite):
    """
    Valida a entrada do usuário para um menu qualquer.
    """

    try:
        valor = int(opcao_escolhida)
    except ValueError:
        return None

    if 0 <= valor <= opcao_limite:
        return valor

    return None
