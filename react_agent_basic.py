import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import TavilySearchResults
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# Carrega .env
load_dotenv()

# Configura o LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Configura a Ferramenta
tools = [TavilySearchResults(max_results=2)]

# Puxa o prompt do Hub
prompt = hub.pull("hwchase17/react")

# CRIAÇÃO DO AGENTE
agent = create_react_agent(llm, tools, prompt)

# EXECUTOR
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True
)

if __name__ == "__main__":
    agent_executor.invoke({"input": "Como está o tempo no Estreito de Ormuz hoje?"})
