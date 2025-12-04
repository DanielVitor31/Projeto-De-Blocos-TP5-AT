from utils.menu_generico import exibir_menu
from funcionarios_tp2.funcionarios_crud_db import funcionarios_criar_resetar
from funcionarios_tp2.funcionarios import *
from constantes.constantes import CONSOLE_REDUZIDO


def menu_exibir_tp2():
    """Menu do TP2 - Funcionários e exercícios."""

    opcoes = {
        1: ("Resetar e Criar Tabela de Funcionários (tudo automatico com dados de exemplo do professor)", funcionarios_criar_resetar),
        2: ("Exibir Funcionário", lambda: funcionarios_exibir(CONSOLE_REDUZIDO)),
        3: ("Selecione todos os funcionários que trabalham no departamento Técnico (Exercico 1).", exercicio1_exibir),
        4: ("Selecione os nomes dos funcionários que possuem um salário maior que 5.000,00 (Exercício 2).", exercicio2_exibir),
        5: ("Selecione o nome e a data de contratação dos funcionários que foram contratados após 01/01/2022. (Exercício 3).", exercicio3_exibir),
        6: ("Selecione o departamento e o salário médio de cada departamento. (Exercício 4).", exercicio4_exibir),
        7: ('Selecione o nome e o cargo dos funcionários que possuem "da Silva" no nome. (Exercício 5).', exercicio5_exibir),
        8: ("Selecione todos os funcionários que têm cargos de confiança. (Exercício 6).", exercicio6_exibir),
        9: ("Selecione o nome e o departamento dos Montador Júnior. (Exercício 7).", exercicio7_exibir),
        10: ("Selecione o nome dos funcionários e seus salários ordenados de forma decrescente pelo salário. (Exercício 8).", exercicio8_exibir),
        11: ("Selecione o nome e o ID dos funcionários que foram contratados no ano de 2023. (Exercício 9).", exercicio9_exibir),
        12: ("Selecione o nome dos funcionários que trabalham no departamento Administração e possuem um salário menor ou igual a 3.000,00. (Exercício 10).", exercicio10_exibir),
        13: ("Selecione o nome dos funcionários que são Coordenador Administrativo ou Diretor. (Exercício 11).", exercicio11_exibir),
        14: ("Selecione o nome dos funcionários e os anos de experiência (considerando que estamos em 2025). (Exercício 12).", exercicio12_exibir),
        15: ("Selecione o nome e o departamento dos funcionários, ordenados pelo nome em ordem alfabética. (Exercício 13).", exercicio13_exibir),
        16: ("Selecione o nome e o cargo dos funcionários cujo nome começa com 'João'. (Exercício 14).", exercicio14_exibir),
        17: ("Selecione a quantidade de funcionários em cada departamento. (Exercício 15).", exercicio15_exibir),
    }

    exibir_menu(
        "MENU TP2 - FUNCIONÁRIOS",
        opcoes,
        texto_sair="Voltar para o Menu Principal",
    )
    print("Você voltou para o Menu Principal.")