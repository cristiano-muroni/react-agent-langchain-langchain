from langgraph.graph import StateGraph, MessagesState, START, END

#import os
#from dotenv import load_dotenv


#load_dotenv()

#model="gemini-2.0-flash", 
#google_api_key=os.getenv("GOOGLE_API_KEY")


def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}


graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

print(graph.invoke({"messages": [{"role": "user", "content": "hi!"}]}))


