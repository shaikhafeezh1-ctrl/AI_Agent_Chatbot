<<<<<<< HEAD
# Step 1 : Setup API Keys for Groq, OPENAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")


# Step 2 : Setup LLM & Tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
#from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch



openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm= ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearch(max_results=2)

# Step 3 : Setup AI Agent with Search tools functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as AI chatbot who is smart and friendly"

def get_respose_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):

    if provider == "Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="openAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt

        )

    
    state={"messages": [("human",query)]}
    response = agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[msg.content for msg in messages if isinstance(msg ,AIMessage)]
    return ai_messages[-1]
=======
# Step 1 : Setup API Keys for Groq, OPENAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")


# Step 2 : Setup LLM & Tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm= ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

# Step 3 : Setup AI Agent with Search tools functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as AI chatbot who is smart and friendly"

def get_respose_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):

    if provider == "Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="openAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt

        )

    
    state={"messages": [("human",query)]}
    response = agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[msg.content for msg in messages if isinstance(msg ,AIMessage)]
    return ai_messages[-1]
>>>>>>> a2777adc1253ce55266434222cd2e7e8ad2d7341
