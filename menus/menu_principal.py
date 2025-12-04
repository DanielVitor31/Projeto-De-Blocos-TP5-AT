from utils.menu_generico import exibir_menu
from .menu_tp1 import menu_exibir_tp1
from .menu_tp2 import menu_exibir_tp2
from .menu_tp3 import menu_exibir_tp3
from .menu_tp4 import menu_exibir_tp4


def menu_exibir():
    """Menu principal do sistema."""

    opcoes = {
        1: ("TP1 (Tarefas)", menu_exibir_tp1),
        2: ("TP2 (Funcionários)", menu_exibir_tp2),
        3: ("TP3 ( Negocio Completo)", menu_exibir_tp3),
        4: ("TP4 ( Inserir/Atualizar e Deletar Clientes JSON)", menu_exibir_tp4),
    }

    exibir_menu("MENU PRINCIPAL", opcoes, texto_sair="Sair do programa")
    print("Você optou por encerrar o programa.")
