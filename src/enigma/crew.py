from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import PDFSearchTool
# from src.enigma.tools.custom_tool import MyOwnRAGTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Enigma():
    """Enigma crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Instanciar la herramienta
    # rag_tool = MyOwnRAGTool()


    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def extractor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['extractor_agent'], # type: ignore[index]
            verbose=True,
            tools=[PDFSearchTool(pdf='src/enigma/documents/ai.pdf')], #RAG TOOL PARA 
        )

    @agent
    def summarizer_agent(self) -> Agent:
       # rag_tool = MyOwnRAGTool()
        return Agent(
            config=self.agents_config['summarizer_agent'], # type: ignore[index]
            verbose=True,
            #tools=[rag_tool]
        )
    
    # @agent
    # def coordinator_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['coordinator_agent'], # type: ignore[index]
    #         verbose=True
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['extraction_task'], # type: ignore[index]
        )

    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'], # type: ignore[index]
            output_file='report.md'
        )
    
    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['compile_final_summary_task'], # type: ignore[index]
    #         output_file='report.md'
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Enigma crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
