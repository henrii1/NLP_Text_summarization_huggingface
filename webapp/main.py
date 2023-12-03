from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel


generator = pipeline('text-generation', model='gpt2')

app = FastAPI()


class Body(BaseModel):
    text: str

@app.get('/')
async def root():
    return Response('<h1>Model designed to interact with gpt2 and generate text</h1>')


@app.post('/generate', response_description = "Generated Text")
async def predict(body: Body):         # output at response body
    results = generator(body.text, max_length= 35, num_returns_sequences = 1)
    return results[0]



