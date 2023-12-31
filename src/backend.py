from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

with open('../prompts/system_instruction.prompt', 'r') as f:
    system_instruction = f.read()

class TableGenerator:
    def __init__(self, system_instruction, engine = 'gpt-3.5-turbo-0613'):
        self.system_instruction = system_instruction
        self.engine = engine

    def _infer_using_chatgpt(self, text):
        messages = [{"role": "system", "content": self.system_instruction},
                {"role": "user", "content": text}]
        response = openai.ChatCompletion.create(model = self.engine,
                                                temperature = 0,
                                                messages=messages) 
        result = response['choices'][0]['message']['content']
        return result
    
    def generate(self, text):
        result = self._infer_using_chatgpt(text)
        return result

app = FastAPI()

class InputData(BaseModel):
    original_text: str

@app.post("/create_vocab_table")
def create_vocab_table(input_data: InputData):

    table_generator = TableGenerator(system_instruction)
    output_table = table_generator.generate(input_data.original_text)
    
    return {"output_table": output_table}

