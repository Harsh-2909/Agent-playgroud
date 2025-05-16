import dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat


dotenv.load_dotenv()

agent = Agent(
    name="Basic",
    model=OpenAIChat(id="gpt-4o-mini"),
    # description="You are a helpful assistant who answers questions.",
    debug_mode=True,
    # markdown=True,
)

agent.print_response(
    "What is the meaning of life",
    stream=True,
)
# response = agent.run(
#     "What is the capital of France? Tell me some interesting facts about that place.",
#     stream=True,
# )
# print(response)
# for chunk in response:
#     print(chunk.content, end="|")
# print("----")
