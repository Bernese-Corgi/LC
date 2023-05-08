import os
import dotenv
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

serp_key = os.environ["SERPAPI_API_KEY"]
openai_key = os.environ['OPENAI_API_KEY']

# 에이전트를 제어하는 ​​데 사용할 언어 모델을 로드
llm = OpenAI(openai_api_key=openai_key)

# 필요한 도구 로드. llm-math 도구는 LLM을 사용하므로 이를 전달해야 한다.
tools = load_tools(
    tool_names=['serpapi', 'llm-math'],
    llm=llm,
    serp_key=serp_key
)

# 도구, 언어모델 및 사용하려는 에이전트 유형으로 에이전트 초기화
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")