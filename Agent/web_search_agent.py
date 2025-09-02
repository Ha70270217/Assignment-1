from agents import Agent
from Tavily_function.function import web_search
from configuration.config import Model






agent = Agent(
 name="General Agent", 
 instructions= "Your are a General Agent",
 tools= [web_search],
 model=Model
)