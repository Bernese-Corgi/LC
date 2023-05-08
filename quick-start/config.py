import os
import dotenv


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

serp_key = os.environ["SERPAPI_API_KEY"]
openai_key = os.environ['OPENAI_API_KEY']