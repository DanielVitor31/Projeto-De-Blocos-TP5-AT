from utils.menu_generico import exibir_menu
from web_scraping.base import exibir


def menu_exibir_tp5():
    """Menu do TP5 - Web Scraping."""

    opcoes = {
        1: ("Web Scraping (Unidades federativas do Brasil)", exibir),
    }

    exibir_menu(
        "MENU TP5 - Web Scraping",
        opcoes,
        texto_sair="Voltar para o Menu Principal",
    )
    print("Você voltou para o Menu Principal.")
