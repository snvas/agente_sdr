from crew import ComplianceCrew

def run_compliance_assistant(pergunta: str):
    crew_instance = ComplianceCrew()

    result = crew_instance.crew().kickoff(inputs={"pergunta": pergunta})

    return result
