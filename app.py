from agent.agentic_workflow import GraphBuilder

app = GraphBuilder()

graph = app.build_graph()

result = graph.invoke({
    "messages": [{"role": "user", "content": "give me the karachi weather info of 1 day"}]
})

print(result)