from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory


# --------------------------- 메모리: 체인 및 에이전트에 상태 추가 -------------------------- #
# 이전의 모든 메시지를 문자열로 압축하는 대신 고유한 메모리 개체로 유지할 수 있다
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI()
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    memory=memory,
    prompt=prompt,
    llm=llm
)

conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
conversation.predict(input="Tell me about yourself.")
