from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langgraph.checkpoint.memory import InMemorySaver 
from langgraph.graph.message import add_messages 
from pydantic import * 
from langgraph.graph import StateGraph, START, END
from typing import * 
from langchain.agents import create_agent 
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents.middleware import *
import operator 
load_dotenv()
Checkpointer=InMemorySaver()





def agentCreation(llm):
       agent= create_agent(
        model=llm, 
        middleware=[SummarizationMiddleware(model=llm, 
                                            
                                            tools=[DuckDuckGoSearchResults()],
                                            trigger=('fraction', .8),
                                            keep=('messages',5))])
       return agent




class ChatSate(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages ]



def GraphTreeBuilder(api_key, model_name):
    llm=ChatOpenAI(api_key=api_key, model=model_name)
    agent=agentCreation(llm=llm)
        
    def ChatNode(state : ChatSate):

        

        mantra = ChatPromptTemplate.from_messages([
            ('system', """You are a helpful pahram chat assisitan, 
                        help the user with answer for his or her message with a polite manner. 
                        Rule:
                            - You get angry if user abuse you strictly 
                            - Give answer for pharmacy ralated question only 
                            - If user asks other questions tell him you are an PharmaAI don't have other knowledge strictly
                            - If user needs some calculation then you can help
                            - If user ask to percribe or advice any medicine for any disease you can help him only saying which   medicnes are suitable for the disase or condition with a specific note that 'I am an AI I can be wrong better to consult a Doctor ot Pharmasist before taking any medication, selfmedication can be harmful I will not be resposible if you ended with any consequences' very very strictly
                            - If the user ask you medicine related information you need to provide him 
                            - If you don't have ans with you search web and give the ans strictly 
                            - You also can help those students who are learing pharmacy 
                            - if they want to know about anything about medicine you should provide them 
            """),

            ('human', "{messages}")
        
        ])
        
        chain = mantra | agent 
        output = chain.invoke({"messages": state['messages']})

        return {'messages': [output["messages"][-1].content]}






    builder = StateGraph(state_schema= ChatSate)

    builder.add_node('chat_message', ChatNode)

    builder.add_edge(START, "chat_message")
    builder.add_edge("chat_message", END)

    graph_tree = builder.compile(checkpointer=Checkpointer)

    return graph_tree





