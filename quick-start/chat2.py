from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


# -------------------------------- 채팅 프롬프트 템플릿 ------------------------------- #
chat = ChatOpenAI()

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# 형식이 지정된 메시지에서 채팅 완성 가져오기
chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())

