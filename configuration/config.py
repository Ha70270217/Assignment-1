from agents import OpenAIChatCompletionsModel,AsyncOpenAI
from decouple import config



Api_key = config ("GEMINI_API_KEY")
Base_url = config ("BASE_URL")

tavily_api_key = config("TAVILY_API_KEY")

MODEL = "gemini-2.0-flash"

gemini_client = AsyncOpenAI(api_key=Api_key,base_url=Base_url)

Model= OpenAIChatCompletionsModel(openai_client=gemini_client,model=MODEL)
