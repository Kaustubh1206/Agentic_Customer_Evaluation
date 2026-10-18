from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import ToolCall

dataset = EvaluationDataset(
    golden=[
        Golden(
            input="I am user123, I would like refund for the book and the pen",
            expected_output="A refund ticket for $30 has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")

            ]
        ),
        Golden(
            input="I am user123, I would like refund for the book",
            expected_output="A refund ticket for $23 has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")

            ]
        ),
        Golden(
            input="I am user123, I would like no refund, I just want to know what I purchased",
            expected_output="No refund tickets where issued. Only a list oof what they bought",
            expected_tools=[
                ToolCall(name="get_user_purchase_history")
            ]
        ),
        Golden(
            input="I am user999, I would like refund for the book",
            expected_output="Tell the user that username is not valid and ask for username again before giving a refund.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history")
            ]
        ),
        Golden(
            input="I am user126, I would like refund for the water_bottle",
            expected_output="No refund given because it is outside of the 30 days guideline",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="get_today_date")
            ]
        ),
        Golden(
            input="I am user126, I would like refund for the water_bottle and backpack",
            expected_output="A refund ticket for $45 has been issued successfully only for the backpack. However for the water_bottle is not eligible for refund because it is outside 30 days return policy",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ]
        ),
        Golden(
            input="I am user126, I would like refund for the sneakers",
            expected_output="No refund was given because you did not purchased this item",
            expected_tools=[
                ToolCall(name="get_user_purchase_history")
            ]
        )
    ]
)