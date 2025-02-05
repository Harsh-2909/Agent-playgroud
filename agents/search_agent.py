import dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

dotenv.load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You are a personal search agent that can help me find latest news from web.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(
    "Find me the latest news related to AI breakthroughs in the last few days",
    stream=True,
)
