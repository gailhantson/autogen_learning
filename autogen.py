import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise ValueError("API key not found! Make sure it's set in the .env file.")


async def main():
    # Create your personal agent
    my_agent = AssistantAgent(
        name="amelia_v01",
        system_message="You are an AutoGen agent that I am building. You are Amelia v.01. You are straightforward, and give succinct responses always.",
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o",
            api_key=api_key,
        )
    )

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break

        # Run the agent and stream responses
        stream = my_agent.run_stream(task=user_input)
        await Console(stream)


# Run the async function properly
if __name__ == "__main__":
    asyncio.run(main())