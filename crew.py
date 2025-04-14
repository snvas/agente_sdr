from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_tool = PDFKnowledgeSource(
    file_paths=['guia_lgpd.pdf', 'lgpd.pdf']
)

llm = LLM(model="gpt-4o-mini", temperature=0)

@CrewBase
class ComplianceCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def especialista_compliance(self) -> Agent:
        return Agent(
            config=self.agents_config['especialista_compliance'],
            verbose=True,
            tools=[],
            llm=llm,
        )
    
    @task
    def responder_pergunta_compliance(self) -> Task:
        return Task(
            config=self.tasks_config["responder_pergunta_compliance"]
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the MquestKnowledge"""
        return Crew(
            agents=[self.especialista_compliance()],
            tasks=[self.responder_pergunta_compliance()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool],
        )