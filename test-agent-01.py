from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
hello_world_agent = Agent(
    model=Ollama(id="llama3.2:1b"),
    description="Web Search Agent demonstrating how to use DuckDuckGo search tool",
    tools=[DuckDuckGoTools()],
)
hello_world_agent.print_response("When does March Madness Start?", stream=True)