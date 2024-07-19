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
    def layout_arquitect(self) -> Agent:
        return Agent(
            config=self.agents_config['layout_arquitect'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def css_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['css_expert'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def html_minifier(self) -> Agent:
        return Agent(
            config=self.agents_config['html_minifier'],
            verbose=True
        )

    @task
    def plan(self) -> Task:
        return Task(
            config=self.tasks_config['plan'],
            agent=self.researcher()
        )

    @task
    def create_html(self) -> Task:
        return Task(
            config=self.tasks_config['create_html'],
            agent=self.layout_arquitect()
        )
    
    @task
    def create_css(self) -> Task:
        return Task(
            config=self.tasks_config['create_css'],
            agent=self.css_expert()
        )

    @task
    def minify_html(self) -> Task:
        return Task(
            config=self.tasks_config['minify_html'],
            agent=self.html_minifier()
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Fraud Detection crew"""
        return Crew(
            agents=[self.researcher(), self.layout_arquitect(), self.css_expert(),  self.html_minifier()],
            tasks=[self.plan(), self.create_html(), self.create_css(), self.minify_html()],
            process=Process.sequential,
            verbose=2
        )
