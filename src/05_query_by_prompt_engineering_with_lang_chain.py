from langchain.chains import LLMMathChain
from langchain.llms import OpenAI
from langchain.agents import AgentType, Tool, initialize_agent, create_csv_agent
from langchain.agents.agent_toolkits import NLAToolkit
from callback_handler import RabbitMQCallbackHandler

import os

open_api_url='http://localhost:5300/swagger/v1/swagger.json'
open_api_url='https://fiscanner-platform.azurewebsites.net/swagger/v1/swagger.json'
speak_api_url='https://api.speak.com/openapi.yaml'


# 1 MODEL
# Initialize the LLM from OpenAI
llm = OpenAI(temperature=0, model_name='text-davinci-003')

# Tools
# Get the tools we are going to use
#
open_api_toolkit = NLAToolkit.from_llm_and_url(
    llm=llm,
    open_api_url=open_api_url)

""" Use the following code snippet to setup auth.
    Please don't use the api key provided here, but get your own.
    You can fetch your own api from an enviroment file or from the environment variables.: 
"""
# requests = Requests(headers={'x-api-key': '<<your api key>>'})
# open_api_toolkit = NLAToolkit.from_llm_and_url(
# llm=llm,
# open_api_url=open_api_url,
# requests=requests)


speak_toolkit = NLAToolkit.from_llm_and_url(
    llm=llm,
    open_api_url=speak_api_url)

# Math tool
llm_math = LLMMathChain(llm=llm)

# initialize the math tool
math_toolkit = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.'
)

# Setup the csv agent used by the chain to get data from csv files 
csv_agent = create_csv_agent(
    llm=llm,
    path='titanic.csv', verbose=True)

# Initialize the csv tool that will be used to answer questions about csv files

csv_toolkit = Tool(
    name='Transactions reader',
    func=csv_agent.run,
    description='Useful for when you need to answer questions about titanic stats.'
)

# Slightly tweak the instructions from the default agent
openapi_format_instructions = """Use the following format:

Context: This agent allows to get information by means of different web api and csv files.
Use description to figure out the best match. 

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: what to instruct the AI Action representative.
Observation: The Agent's response
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer. User can't see any of my observations, API responses, links, or tools.
Final Answer: the final answer to the original input question with the right amount of detail."""


natural_language_tools = speak_toolkit.get_tools() + open_api_toolkit.get_tools()

# natural_language_tools.append(math_toolkit)
natural_language_tools.append(csv_toolkit)

# Set customized agent
mrkl = initialize_agent(natural_language_tools,
                        llm,
                        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                        verbose=True,
                        agent_kwargs={"format_instructions": openapi_format_instructions})


callback = RabbitMQCallbackHandler()

mrkl.run("Giovanni planned an 8 funny days trip to Tokyo can you setup a trip plan? Please.",
         callbacks=[callback])


# mrkl.run("Mi consigli un casco per moto?")
# mrkl.run("La mamma mi manda a comprare 3 mele 2 pere e 50 uova. Le mele costano 10 euro l'una, le pere 15 euro l'una e le uova 0.5 euro l'una. Mi dici quanto ho speso in tutto?")
