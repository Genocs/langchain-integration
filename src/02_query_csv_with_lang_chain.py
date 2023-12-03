from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains.base import Chain

from typing import Dict, List


class GenocsCsvChain(Chain):
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        # Union of the input keys of the two chains.
        all_input_vars = set(self.chain_1.input_keys).union(
            set(self.chain_2.input_keys))
        return list(all_input_vars)

    @property
    def output_keys(self) -> List[str]:
        return ['concat_output']

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        output_1 = self.chain_1.run(inputs)
        output_2 = self.chain_2.run(inputs)
        return {'concat_output': output_1 + output_2}


# 1 MODEL
# Initialize the LLM from OpenAI
llm = OpenAI(temperature=0, model_name="text-davinci-003")


# Setup the agent, in this case a csv agent
agent = create_csv_agent(
    llm=llm, 
    path='titanic.csv', 
    verbose=True)


# Run the query
agent.run("Can you check whether there is a correlation between fare and dead or not, please.")