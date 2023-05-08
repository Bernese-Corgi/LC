from langchain import ConversationChain, OpenAI
from config import openai_key


llm = OpenAI(openai_api_key=openai_key)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")

print(output)