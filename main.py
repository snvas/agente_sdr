import pysqlite3
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
from crew import SalesCrew
from config import load_config

def run_sales_development(pergunta: str, inputs: dict = None):
    """
    Executa o processo de desenvolvimento de vendas usando a equipe de agentes.
    
    Args:
        pergunta (str): A pergunta ou contexto principal para análise.
        inputs (dict, optional): Informações adicionais sobre o lead. Defaults to None.
    
    Returns:
        str: O resultado da análise e recomendações.
    """
    try:
        crew_instance = SalesCrew()
        
        if inputs is None:
            inputs = {}
        
        # Combine the question with the lead information
        full_inputs = {
            "pergunta": pergunta,
            **inputs
        }

        result = crew_instance.crew().kickoff(inputs=full_inputs)
        return result
    except Exception as e:
        return f"Erro ao processar a solicitação: {str(e)}"
