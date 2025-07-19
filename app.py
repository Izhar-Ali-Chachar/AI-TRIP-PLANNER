from agent.agentic_workflow import GraphBuilder

app = GraphBuilder()

graph = app.build_graph()

result = graph.invoke({
    "messages": [{"role": "user", "content": "What’s the budget for a 7-day solo trip to Thailand?"}]
})

print(result)