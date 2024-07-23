from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class CompanyResearchCrew():
    """Company Research crew configured to create a web site of a queried company."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['formatter'],
            verbose=True
        )

    @task
    def plan(self) -> Task:
        return Task(
            config=self.tasks_config['plan'],
            agent=self.researcher()
        )

    @task
    def format_content(self) -> Task:
        return Task(
            config=self.tasks_config['format_content'],
            agent=self.formatter()
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Company Researcher crew"""
        return Crew(
            agents=[self.researcher(), self.formatter()],
            tasks=[self.plan(), self.format_content()],
            process=Process.sequential,
            verbose=2
        )
