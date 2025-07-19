from agent.agentic_workflow import GraphBuilder
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from pprint import pprint

app = FastAPI()

class UserQuery(BaseModel):
    user_input: Annotated[str, Field(..., description='user gives input')]

@app.get('/')
def home():
    return {'message': 'home of web'}

@app.post('/generate')
def generator(user_query: UserQuery):
    graph_builder = GraphBuilder()
    graph = graph_builder.build_graph()

    input = user_query.user_input

    result = graph.invoke({
        "messages": [{"role": "user", "content": input}]
    })

    return {"response": result["messages"][-1].content}