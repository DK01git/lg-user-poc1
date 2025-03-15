from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Fromuser():
	"""Fromuser crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def data_collector(self) -> Agent:
		return Agent(
			config=self.agents_config['data_collector'],
			verbose=True
		)

	@agent
	def web_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['web_researcher'],
			verbose=True
		)

	@agent
	def linkedin_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['linkedin_specialist'],
			verbose=True
		)

	@agent
	def github_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['github_analyst'],
			verbose=True
		)

	@agent
	def content_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['content_analyst'],
			verbose=True
		)

	@agent
	def data_synthesizer(self) -> Agent:
		return Agent(
			config=self.agents_config['data_synthesizer'],
			verbose=True
		)

	@agent
	def persona_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['persona_generator'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def initial_data_collection_task(self) -> Task:
		return Task(
			config=self.tasks_config['initial_data_collection_task'],
			agent=self.data_collector()
		)

	@task
	def general_web_search_task(self) -> Task:
		return Task(
			config=self.tasks_config['general_web_search_task'],
			agent=self.web_researcher()
		)

	@task
	def linkedin_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['linkedin_analysis_task'],
			agent=self.linkedin_specialist()			
		)

	@task
	def github_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['github_analysis_task'],
			agent=self.github_analyst()
		)

	@task
	def medium_content_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['medium_content_analysis_task'],
			agent=self.content_analyst()
		)

	@task
	def data_synthesis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_synthesis_task'],
			agent=self.data_synthesizer()
		)

	@task
	def persona_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['persona_generation_task'],
			agent=self.persona_generator(),
			output_file='output/user_persona.json'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Fromuser crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
