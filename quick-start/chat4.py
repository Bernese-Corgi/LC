from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

# ------------------------------- 채팅 모델이 있는 상담원 ------------------------------ #
# 에이전트를 제어하는 ​​데 사용할 언어 모델을 로드
chat = ChatOpenAI()

# 사용할 몇 가지 도구를 로드. `llm-math` 도구는 LLM을 사용하므로 이를 전달해야 합니다.
llm = OpenAI()
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 도구, 언어 모델 및 사용하려는 에이전트 유형으로 에이전트를 초기화
agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")
