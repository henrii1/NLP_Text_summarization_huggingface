import fire
from transformers import pipeline

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]['summary_text']
    return summary


if __name__ == '__main__':
  fire.Fire(predict)