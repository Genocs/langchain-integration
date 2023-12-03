from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

""" PromptTemplate with two paramentes"""
prompt = PromptTemplate(
    input_variables=["product", "language"],
    template="What is a good name for a company that makes {product}?. Remember to replay translated in {language}",
)

# text = prompt.format(product="colorful socks")
# print(text)

llm = OpenAI(temperature=0, model_name="text-davinci-003")
# print(llm(text))

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(product="Colorful socks", language="Francaise"))
