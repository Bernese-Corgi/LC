from llm import llm
from promptTemplate import prompt
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))