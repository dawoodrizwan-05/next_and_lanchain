from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class ResponseData(BaseModel):
    response: str

@app.post("/prompt/")
async def handle_prompt(prompt_data: PromptRequest):
    # Process the user prompt here (for now, echoing back the prompt)
    response_text = f"You said: {prompt_data.prompt}"
    return ResponseData(response=response_text)
