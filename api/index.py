# # from driver import get_completion
# #importing key from api_key.py
from api_key import key
import openai

openai.api_key = key
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# if __name__ == "__main__":
#     response = get_completion("who are you and who made you ?")
#     # response = 'hello'
#     print(response)

from fastapi import FastAPI, HTTPException
from driver import get_completion

app = FastAPI()

@app.post("/get_completion")
async def get_completion_route(prompt: str):
    try:
        response = get_completion(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
