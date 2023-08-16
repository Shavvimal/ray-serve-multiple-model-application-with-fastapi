from transformers import pipeline
from ray import serve

import os
os.system('')

@serve.deployment
class Summarizer:
    def __init__(self):
        # Load model
        self.model = pipeline("summarization", model="t5-small")

    def summarize(self, text: str) -> str:
        # Run inference
        model_output = self.model(text, min_length=5, max_length=15)
        # Post-process output to return only the summary text
        summary = model_output[0]["summary_text"]
        return summary