from langchain.chat_models import ChatOpenAI
from langchain.schema.agent import AgentFinish
from langchain.tools import tool
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.schema.runnable import RunnablePassthrough
from langchain.agents import AgentExecutor

import requests
from pydantic import BaseModel, Field
from langchain.agents import AgentExecutor
import datetime
from sympy import *
import numpy as np
import sympy as sp


from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
import os
import openai
from sympy import symbols,lcm,Poly,factor,sympify,gcd,div

# importing functions from agents.py
from agents import *
from agents import tools

#importing key from api_key.py
from api_key import key

openai.api_key = key
ChatOpenAI(temperature=0,model="gpt=3.5-turbo 0613",openai_api_key=openai.api_key)

#formatting tools to OPENAI functions so that they are callable for chatgpt which is finetuned on such functions
functions = [format_tool_to_openai_function(f) for f in tools]


#making model
model = ChatOpenAI(temperature=0,openai_api_key=openai.api_key).bind(functions=functions)
#making prompt template 


from langchain.prompts import MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    # ("system", "You are helpful but sassy assistant"),
    ("system", "You are a math teacher created by DAT ML that teaches math to the student in very simple and easy way you give a sudo formula. And try to guide them step by step so that students dont get confused in any step. and you also tell them some thing intresting extra knowledge about the qustion"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


#defining chain
chain = prompt | model | OpenAIFunctionsAgentOutputParser()


agent_chain = RunnablePassthrough.assign(
    agent_scratchpad= lambda x: format_to_openai_functions(x["intermediate_steps"])
) | chain

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def run_agent(user_input):
    intermediate_steps = []
    while True:
        result = agent_chain.invoke({
            "input": user_input, 
            "intermediate_steps": intermediate_steps
        })
        if isinstance(result, AgentFinish):
            return result
        tool = {
            "Matrix_Product":Matrix_Product,
            "Inverse_Of_Matrix":Inverse_Of_Matrix,
            "Matrix_Adj":Matrix_Adj,
            "Matrix_Det":Matrix_Adj,
            "isRationalExpression":isRationalExpression,
            "SubstituteInExpression":SubstituteInExpression,
            "is_Polynomial":is_Polynomial,
            "ReducedToLowestForm":ReducedToLowestForm
            
        }[result.tool]
        observation = tool.run(result.tool_input)
        intermediate_steps.append((result, observation))

agent_executor = AgentExecutor(agent=agent_chain, tools=tools, verbose=True)

# agent_executor.invoke("hello")