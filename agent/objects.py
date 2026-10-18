from pydantic import BaseModel, Field

class Answer(BaseModel):
    answer:str = Field(description="The answer that is needef for the user question")
    # Whether the conversation should continue or not 
    conversation:bool = Field(description="This is an indicator to know if the conversation should still continue or not. If the agent has made the decision about refund this should be False. If the conversation still need more talk then its True",default=True) 


# For our model to know how to pass the reponse to other model in structured format
class PurchaseItem(BaseModel):
    name : str = Field(description="Name of the item purchased")


