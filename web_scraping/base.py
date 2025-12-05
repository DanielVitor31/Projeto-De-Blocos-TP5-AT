from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime
from models.models_tp5 import Pagina_models, Estado_models, ErroScraping_models
import re

from conexao import conectar, desconectar
from sqlalchemy import select, func



URL = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
"""
Inicialmente eu ia fazer de algo relacionado a computação ou ao meu projeto, porém essa parada de juntar com o sql complicou um pouco
peguei o wiki parecido com o do professor de python e tentei fazer meu melhor.
Nesse dia que estou entregando o banco de dados está lento e com frescura então n testei 100%, porém fiz meu melhor 
"""

# ========= WEB SCRAPING =========

def acessar_url():
    try:
        request = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(request)
        html = response.read()
        return html
    except Exception as ex:
        raise RuntimeError(f"Erro ao acessar a URL: {ex}")


def exibir_titulo(bs):
    titulo = bs.title.text if bs.title else None
    if not titulo:
        print("Erro: título não existe")
        return None
    print("Título da página:", titulo)
    return titulo


def obter_tabela(bs):
    # pega todas as tabelas que contenham "wikitable" em qualquer combinação de classes
    tabelas = bs.find_all("table", class_=lambda c: c and "wikitable" in c)

    if not tabelas:
        print("Nenhuma wikitable encontrada.")
        return []

    tabela_certa = None

    # identifica a tabela pelo cabeçalho (blindado contra mudanças)
    for tabela in tabelas:
        headers = [th.get_text(strip=True).lower() for th in tabela.find_all("th")]

        if ("unidade federativa" in headers) and ("abrev." in headers) and ("capital" in headers):
            tabela_certa = tabela
            break

    if tabela_certa is None:
        print("Tabela de estados não encontrada.")
        return []

    linhas = tabela_certa.find_all("tr")
    estados = []

    for linha in linhas[1:]:  # pula header
        colunas = linha.find_all(["th", "td"])
        if len(colunas) < 3:
            continue

        nome = colunas[0].get_text(strip=True)
        sigla = colunas[1].get_text(strip=True)
        capital = colunas[2].get_text(strip=True)

        # remove [1], [2] etc...
        nome = re.sub(r"\[\d+\]", "", nome)
        capital = re.sub(r"\[\d+\]", "", capital)

        estados.append({
            "nome": nome,
            "sigla": sigla,
            "capital": capital
        })

    return estados




# ========= HELPER =========

def _rodar_exercicio(consulta_fn):
    try:
        session = conectar()
        print("Fazendo buscas no banco de dados aguarde....")

        resultado = consulta_fn(session)

        if not resultado:
            print("Nenhum registro encontrado.")
            return

    except Exception as ex:
        print("Deu erro para exibir os registro: ", ex)
        return

    finally:
        try:
            desconectar(session)
        except UnboundLocalError:
            pass

    return resultado


# ========= PROCESSAR / SALVAR SCRAPING =========

def processar_pagina():
    """
    Faz o scraping, salva na tabela paginas, estados e
    registra erro em erros_scraping se der ruim.
    """
    session = conectar()

    try:
        html = acessar_url()
        bs = BeautifulSoup(html, "lxml")

        titulo = exibir_titulo(bs) or "Sem título"
        estados = obter_tabela(bs)

        # cria registro em paginas
        pagina = Pagina_models(
            url=URL,
            titulo=titulo,
            data_hora=datetime.now(),
            status_code=None, 
            sucesso=True,
        )
        session.add(pagina)
        session.flush()  

        # cria registros em estados
        for e in estados:
            estado = Estado_models(
                pagina_id=pagina.id_pagina,
                nome=e["nome"],
                sigla=e["sigla"],
                capital=e["capital"],
            )
            session.add(estado)

        session.commit()

        print("\nEstados encontrados:")
        for e in estados:
            print(f"{e['sigla']:>2} - {e['nome']} (capital: {e['capital']})")

    except Exception as ex:
        session.rollback()

        # registra erro em tabela
        erro = ErroScraping_models(
            url=URL,
            mensagem=str(ex),
            data_hora=datetime.now(),
        )
        session.add(erro)
        session.commit()

        print("Erro durante o scraping, registrado em erros_scraping:", ex)

    finally:
        desconectar(session)


# ========= INNER JOIN / AGRUPAMENTO =========

def listar_estados_com_pagina():
    """
    INNER JOIN estados x paginas
    """
    def consulta(session):
        stmt = (
            select(
                Estado_models.nome,
                Estado_models.sigla,
                Estado_models.capital,
                Pagina_models.url,
                Pagina_models.data_hora,
            )
            .join(
                Pagina_models,
                Pagina_models.id_pagina == Estado_models.pagina_id,
            )
        )
        return session.execute(stmt).mappings().all()

    return _rodar_exercicio(consulta_fn=consulta)


def relatorio_erros_por_url():
    """
    SELECT url, COUNT(*) AS qtd_falhas
    FROM erros_scraping
    GROUP BY url;
    """
    def consulta(session):
        stmt = (
            select(
                ErroScraping_models.url,
                func.count(ErroScraping_models.id_erro).label("qtd_falhas"),
            )
            .group_by(ErroScraping_models.url)
        )
        return session.execute(stmt).mappings().all()

    return _rodar_exercicio(consulta_fn=consulta)


def resumo_paginas():
    """
    Exemplo de métricas:
    - total de páginas
    - quantas com sucesso
    - quantas com falha
    """
    def consulta(session):
        total = session.execute(
            select(func.count(Pagina_models.id_pagina))
        ).scalar_one()

        sucesso = session.execute(
            select(func.count(Pagina_models.id_pagina)).where(Pagina_models.sucesso == True)
        ).scalar_one()

        falha = total - sucesso

        return {
            "total_paginas": total,
            "paginas_sucesso": sucesso,
            "paginas_falha": falha,
        }

    return _rodar_exercicio(consulta_fn=consulta)


def exibir():
    # 1) roda scraping e salva no banco
    processar_pagina()

    # 2) exemplos de consultas
    print("\n--- Estados com info da página ---")
    for row in listar_estados_com_pagina() or []:
        print(row)

    print("\n--- Falhas por URL ---")
    for row in relatorio_erros_por_url() or []:
        print(row)

    print("\n--- Resumo páginas ---")
    print(resumo_paginas())
