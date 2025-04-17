from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from tools import web_search, sentiment_tool


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=2000,
    streaming=True
)

@CrewBase
class SalesCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def sales_rep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_rep_agent'],
            verbose=True,
            tools=[web_search],
            llm=llm,
        )

    @agent
    def lead_sales_rep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_sales_rep_agent'],
            verbose=True,
            tools=[sentiment_tool, web_search],
            llm=llm,
        )

    @task
    def lead_profiling_task(self) -> Task:
        task_config = self.tasks_config["lead_profiling_task"]
        return Task(
            description=task_config["description"],
            expected_output=task_config["expected_output"],
            tools=[web_search],
            agent=self.sales_rep_agent()
        )

    @task
    def personalized_outreach_task(self) -> Task:
        task_config = self.tasks_config["personalized_outreach_task"]
        return Task(
            description=task_config["description"],
            expected_output=task_config["expected_output"],
            tools=[web_search, sentiment_tool],
            agent=self.lead_sales_rep_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Sales Development Crew"""
        return Crew(
            agents=[self.sales_rep_agent(), self.lead_sales_rep_agent()],
            tasks=[self.lead_profiling_task(), self.personalized_outreach_task()],
            process=Process.sequential,
            verbose=True,
        )