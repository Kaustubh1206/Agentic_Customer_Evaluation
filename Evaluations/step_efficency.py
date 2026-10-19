import sys
from pathlib import Path
from uuid import uuid4

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "agent")
)

from agent import agent
from dataset import dataset
from model import eval_model

from deepeval.metrics import StepEfficiencyMetric
from deepeval.integrations.langchain import CallbackHandler

SUCCESSFUL_TASK_DESCRIPTION = """

"""

# threshold -> how accurate and complex you want model to behave. Pass or fail
metrics = [StepEfficiencyMetric(threshold=0.8,model=eval_model, include_reason=True)]


# eval_iterator allows to evaluate dataset in asynchronous way
for golden in dataset.evals_iterator(metrics=metrics):
    response = agent.invoke(
        {"messages":[{"role":"user","content":golden.input}]},
        config={"configurable":{"thread_id":str(uuid4())},"callbacks":[CallbackHandler()]} # get back what agent is saying . run on metric
    )