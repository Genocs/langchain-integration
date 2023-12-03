from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
from langchain.agents import create_csv_agent


template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    """This function is called when the chat starts."""

    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = OpenAI(temperature=0, model_name="gpt-4")
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    csv_agent = create_csv_agent(llm=llm, 
                                 path='./src/titanic.csv', 
                                 verbose=True)

    # Store the chain in the user session
    cl.user_session.set("csv_agent", csv_agent)



@cl.on_message
async def main(message: str):
    """This function is called when the user sends a message."""
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("csv_agent")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Do any post processing here

    # "res" is a Dict. For this chain, we get the response by reading the "text" key.
    # This varies from chain to chain, you should check which key to read.
    await cl.Message(content=res["text"]).send()
