from conexao import conectar, desconectar
from sqlalchemy import text, func, select
from models.models_tp3 import *



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
        # garante que session sempre existe antes de tentar desconectar
        try:
            desconectar(session)
        except UnboundLocalError:
            pass
        
    resultado_tratado = resultado

    return resultado_tratado

    
def inner_join():
    """"
    Exibir todos os funcionarios e suas montagens
    OBS: Eu poderia agrupar pelo id do funcionario, mas fiz assim para n perder a lógica de N:N
    
    Versão SQL puro:
    SELECT
    f.id_funcionario,
    f.nome,
    f.cargo,
    mf.xid_montagem
    FROM projeto_de_bloco_tp3.montagem_funcionario mf
    INNER JOIN projeto_de_bloco_tp3.funcionarios f ON f.id_funcionario = mf.xid_funcionario;
    """
    def consulta(session):
        stmt = (
        select(
            Funcionarios_models.id_funcionario,
            Funcionarios_models.nome,
            Funcionarios_models.cargo,
            MontagemFuncionario_models.xid_montagem,
        )
        .join(
            Funcionarios_models,
            Funcionarios_models.id_funcionario == MontagemFuncionario_models.xid_funcionario,
        )
        )
        
        return (
            session.execute(stmt).mappings().all()
        )

    return _rodar_exercicio(consulta_fn=consulta)   
 
    
def left_join():
    """"
    Exibir todas montagens independente dos funcionarios
    Versão SQL puro:
    SELECT
    m.id_montagem,
    m.placa_mae,
    m.placa_video,
    m.processador,
    m.total,
    f.id_funcionario,
    f.nome AS nome_funcionario,
    f.cargo
    FROM projeto_de_bloco_tp3.montagem m
    LEFT JOIN projeto_de_bloco_tp3.montagem_funcionario mf ON mf.xid_montagem = m.id_montagem
    LEFT JOIN projeto_de_bloco_tp3.funcionarios f ON f.id_funcionario = mf.xid_funcionario;
    
    """
    def consulta(session):
        stmt = (
            select(
                Montagem_models.id_montagem,
                Montagem_models.placa_mae,
                Montagem_models.placa_video,
                Montagem_models.processador,
                Montagem_models.total,
                Funcionarios_models.id_funcionario,
                Funcionarios_models.nome.label("nome_funcionario"),
                Funcionarios_models.cargo,
            )
            .outerjoin(
                MontagemFuncionario_models,
                MontagemFuncionario_models.xid_montagem == Montagem_models.id_montagem,
            )
            .outerjoin(
                Funcionarios_models,
                Funcionarios_models.id_funcionario == MontagemFuncionario_models.xid_funcionario,
            )
    )
        
        return (
            session.execute(stmt).mappings().all()
        )

    return _rodar_exercicio(consulta_fn=consulta)   
    
def right_join():
    """"
    Exibir todos os funcionarios independente das montagens.
    OBS: SQLAlchemy não possui RIGHT JOIN direto, mas pode ser feito com LEFT JOIN invertido
    Versão SQL puro:
    
    SELECT f.id_funcionario, f.nome, mf.xid_montagem 
    FROM projeto_de_bloco_tp3.montagem_funcionario mf 
    RIGHT JOIN projeto_de_bloco_tp3.funcionarios f ON f.id_funcionario = mf.xid_funcionario;
    """
    def consulta(session):
        stmt = (
        select(
            Funcionarios_models.id_funcionario,
            Funcionarios_models.nome,
            MontagemFuncionario_models.xid_montagem,
        )
        .outerjoin(
            MontagemFuncionario_models,
            MontagemFuncionario_models.xid_funcionario == Funcionarios_models.id_funcionario,
        )
        )
        
        return (
            session.execute(stmt).mappings().all()
        )

    return _rodar_exercicio(consulta_fn=consulta)   
    
