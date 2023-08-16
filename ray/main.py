from ray import serve
from ray.serve.handle import RayServeHandle
from fastapi import FastAPI
from pydantic import BaseModel

from models import Translator, Summarizer
from utils import p

import os 
os.system('')

class TranslationItem(BaseModel):
    text: str

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()

@serve.deployment
@serve.ingress(app)
class FastAPIDeployment:
    def __init__(self, translator: RayServeHandle, summarizer: RayServeHandle):
        # Load model
        self.summarizer = summarizer
        self.translator = translator

    @app.get("/")
    def root(self):
        return "Hello, world!"

    @app.post("/{subpath}")
    def root(self, subpath: str):
        return f"Hello from {subpath}!"
    
    @app.post("/translate/")
    async def translate(self, translationItem: TranslationItem) -> str:
        print("Translate")
        summary_ref = await self.summarizer.summarize.remote(translationItem.text)
        summary = await summary_ref
        # self.translator.translate.remote(summary) issues an asynchronous call to the Translator’s translate method.
        # The line immediately returns a reference to the method’s output, 
        translation_ref = await self.translator.translate.remote(summary)
        # waits for translate to execute and returns the value of that execution.
        translation = await translation_ref
        return translation

app = FastAPIDeployment.bind(Translator.bind(), Summarizer.bind())