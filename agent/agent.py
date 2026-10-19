from models import model
from tools import calculate_right_refund,get_today_date,get_user_purchase_history
from dotenv import load_dotenv
from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from uuid import uuid4

load_dotenv()


agent = create_agent(
    model=model,
    system_prompt=agent_system_prompt,
    tools=[calculate_right_refund,get_today_date,get_user_purchase_history],
    response_format=Answer,
    checkpointer=InMemorySaver()
)

def run_conversation():

    # To get know which conversation is going on and prevent memory leak
    config={"configurable": {"thread_id": str(uuid4())}} # every conversation will have a specific uuid
    text="I would like to request a refund"
    print(text)
    question = HumanMessage(content=text)
    conversation=True

    while conversation:
        response = agent.invoke({"messages":question},config=config)
        structured_response = response['structured_response']

        print(structured_response.answer)

        conversation = structured_response.conversation

        if conversation:
            user_input = input("reply: \n")
            question = HumanMessage(content=user_input)

    print("The job is done")


# run_conversation()
