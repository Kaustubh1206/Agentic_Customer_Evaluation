from langchain.tools import tool
from data import users_data
from dotenv import load_dotenv
import logging
from objects import PurchaseItem
from datetime import date

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@tool
# usr will be string 
def get_user_purchase_history(user: str) -> dict:
    """This tool takes user's username and return a dict of the user purchase history. If the user exist."""
    logging.info(f"Using get_user_purchase_history tool on user: {user}")
    if users_data.get(user):
        return users_data[user]
    return {"status":"There was no username found"}


# There can be some users who want to know whether they are eligible for refund ?
# Or How much refund they will get ?
@tool
def calculate_right_refund(user:str, items:list[PurchaseItem])->str:
    """    Check the requested purchased items against the
    30-day refund policy.

    Return the eligible refund total and an eligibility
    decision for each item.

    Call this before issuing any refund ticket."""
    logging.info(f"Using calculate_right_refund tool to get user's: {user} refund")
    if users_data.get(user):
        total_refund = 0

        for item in items:
            # verify user item exists
            if users_data[user].get(item.name):
                total_refund += users_data[user][item.name]["price"]
        return f"The value of the refund is : {total_refund}"
    return {"status":"No username found"}
        
    

@tool 
def issue_refund_ticket(user:str ,refund_amount: int)->str:
    """
    This tool will send a ticket to the right team to return the refund
    """
    logging.info(f"Using issue_refund_tickets for user: {user}")
    return f"A refund ticket has been issued succesfully with amount of {refund_amount}"


@tool 
def get_today_date() ->str:
    """
    Return todays date in YYYY-MM-DD Format
    This tool takes no arguments 
    """
    logging.info(f"Using the date tool")
    return date.today()

book=PurchaseItem(name="book")
pen=PurchaseItem(name="pen")

# print(get_user_purchase_history.invoke("user123"))
# print(calculate_right_refund.invoke({"user":"user123","items":[book,pen] }))
# print(issue_refund_ticket.invoke({"user":"user123","refund_amount":30}))
# print(get_today_date.invoke("user123"))