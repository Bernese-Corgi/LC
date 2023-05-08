import os
import dotenv
from langchain.llms import OpenAI

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

key = os.environ['OPENAI_API_KEY']

llm = OpenAI(openai_api_key=key)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
