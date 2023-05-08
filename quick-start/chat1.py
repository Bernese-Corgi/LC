from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from config import openai_key


chat = ChatOpenAI(openai_api_key=openai_key)

# ---------------------------- 채팅 모델에서 메시지 완성 가져오기 --------------------------- #
# 단일 메시지
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]

print('단일 메시지')
chat(messages=messages)

# 여러 메시지 집합
batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love artificial intelligence.")
    ]
]

print('여러 메시지 집합')
result = chat.generate(batch_messages)
result
# LLMResult에서 토큰 사용과 같은 항목을 복구할 수 있습니다.
result.llm_output['token_usage']

