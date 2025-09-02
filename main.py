from agents import Runner,set_tracing_disabled,RunConfig
from Agent.web_search_agent import agent

set_tracing_disabled(True)

prompt = input("Enter your question: ")

result =Runner.run_sync(starting_agent=agent,input=prompt)
print(result.final_output)
