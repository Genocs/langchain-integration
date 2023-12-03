from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import NLAToolkit
from callback_handler import RabbitMQCallbackHandler
import os

class FiscannerIntegration:
    def __init__(self):
        self._openapi_format_instructions = None
        self._agent = None

    def initialize(self):
        self.__setup_instructions()
        self.__setup_components()

    def __setup_instructions(self):
        """This method is used to setup the instructions for the LLM."""

        # Read the instruction to give to the LLM from text file called "instructions.txt" that is in the project root folder
        instructions_file_path = os.path.join(
            os.path.dirname(__file__), 'instructions.txt')
        if os.path.exists(instructions_file_path):
            with open(instructions_file_path, 'r') as f:
                self._openapi_format_instructions = f.read()

    def __setup_components(self):
        """This method is used to setup the components for the LLM."""

        # 1 MODEL: Initialize the LLM from OpenAI
        llm = OpenAI(temperature=0, model_name='text-davinci-003')             

        # 2 TOOLS: Get the tools we are going to use
        fiscanner_toolkit = NLAToolkit.from_llm_and_url(
            llm=llm,
            f"amqps://{os.getenv('FISCANNER_URL')}/swagger/v1/swagger.json")

        """ Use the following code snippet to setup auth 
        """
        # requests = Requests(headers={'x-api-key': '<<your api key>>'})
        # fiscanner_toolkit = NLAToolkit.from_llm_and_url(
        #     llm=llm,
        #     f"amqps://{os.getenv('FISCANNER_URL')}/swagger/v1/swagger.json",
        #     requests=requests)


        natural_language_tools = fiscanner_toolkit.get_tools()

        # Set customized agent
        self._agent = initialize_agent(natural_language_tools,
                                llm,
                                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                verbose=True,
                                agent_kwargs={"format_instructions": self._openapi_format_instructions})

        self._callback = RabbitMQCallbackHandler()

    def run(self, question : str):
        """This method is used to run the query."""
        # Check if the components are initialized by lookng at the self._agent variable if it is None or not
        if self._agent is None:
            self.initialize()

        # 3 RUN: Run the LLM
        self._agent.run(question, callbacks=[self._callback])
