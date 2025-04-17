from crew import SalesCrew

def run_sales_development(pergunta: str, inputs: dict = None):
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
