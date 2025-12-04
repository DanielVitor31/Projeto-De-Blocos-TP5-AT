from constantes.constantes import MENU_SAIR, LIMPAR_MENUS
from utils.menu_utils import menu_validar_entrada, limpar_tela


def exibir_menu(titulo, opcoes, texto_sair="Voltar"):

    if not opcoes:
        raise ValueError("O dicionário de opções do menu não pode ser vazio.")

    opcao_max = max(opcoes.keys())
    if LIMPAR_MENUS:
                limpar_tela()
    while True:
        

        print("=" * 40)
        print(titulo)
        print("=" * 40)

        for numero in sorted(opcoes.keys()):
            descricao, _ = opcoes[numero]
            print(f"[{numero}] {descricao}")

        print(f"[{MENU_SAIR}] {texto_sair}")

        entrada = input("Digite a opção desejada: ")
        opcao = menu_validar_entrada(entrada, opcao_max)

        if opcao is None:
            print("Opção inválida, tente novamente.")
            continue

        if opcao == MENU_SAIR:
            if LIMPAR_MENUS:
                limpar_tela()
            return

        _, funcao = opcoes.get(opcao, (None, None))

        if funcao is None:
            print("Opção não implementada.")
            continue


        funcao()

