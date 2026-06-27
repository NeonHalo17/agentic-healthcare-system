from langchain.evaluation.qa import QAEvalChain

from config.llm_config import get_llm


class QAEvaluator:

    def __init__(self):
        self.chain = QAEvalChain.from_llm(get_llm())

    def evaluate(self,question,prediction,reference):

        examples = [
            {
                "query": question,
                "answer": reference
            }
        ]

        predictions = [
            {
                "result": prediction
            }
        ]

        return self.chain.evaluate(examples,predictions)[0]
