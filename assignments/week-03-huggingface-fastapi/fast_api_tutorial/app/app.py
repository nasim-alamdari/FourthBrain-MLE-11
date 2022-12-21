# please check out http://localhost:8000/docs#/default/translate_translate_post for the api
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline


pipeline = pipeline(model="t5-small")


app1 = FastAPI()

@app1.get("/") # this is decrators
def index():
    return {"message": "Hello World"}

"""@app1.get("/cool") # this is decrators
def cool_stuff():
    return {"message": "this is me!"}"""

@app1.get("/ping")
def ping():
    return {"message": "pong"}


class TextToTranslate(BaseModel):
    input_text: str
    
class TextsToTranslate(BaseModel):
    input_texts: List[str]
    
#@app1.post("/echo") # this is decrators
#def echo(message:str):
#    return {"echo": message}

@app1.post("/echo") # this is decrators
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app1.post("/translate") # this is decrators
def translate(texts_to_translate: TextsToTranslate):
    return {"message": pipeline(texts_to_translate.input_texts)}

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app1", host="0.0.0.0", port=8000, reload=True)