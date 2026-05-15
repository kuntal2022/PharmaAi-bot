import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from backend import GraphTreeBuilder, agentCreation
from style_type import set_page_config, mainpageStyle, chatInputStyle, sidebarStyle, userAIStyle, newStyle




st.header("⚕️Pharma-AI")
st.text('Creator - Kuntal')

set_page_config()
mainpageStyle()
chatInputStyle()
sidebarStyle()
userAIStyle()
newStyle()

st.image(r"C:\Users\kuntal.chakraborty\Downloads\pimage.png")

if "message_history" not in st.session_state:
    st.session_state['message_history'] =  []



for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

human_input=st.chat_input("Write Here")

flag=False

model_name=st.sidebar.selectbox(label="Select Model", options=['gpt-4.1', 'gpt-3.5-turbo', 'gpt-5.1-mini', 'gpt-4.1-mini', 'gpt-4o'])
st.sidebar.write(f"Model Selected: {model_name}")
st.sidebar.text("............................................................")



open_api_key=st.sidebar.text_input('🔑 Open AI API KEY', type='password')
if len(open_api_key)>40:
    flag=True

    if "graph_tree" not in st.session_state:
        st.session_state['graph_tree'] =  GraphTreeBuilder(api_key=open_api_key, model_name=model_name)
        
        

 
    
        st.sidebar.write("✅ API KEY IS Varified")
else:
     st.sidebar.write("❌ Please Give a Correct OpenAI API KEY ")
thread_id=st.sidebar.text_input('🧑‍🦰 Name')
st.sidebar.write(f"Welcome {thread_id}")

age = st.sidebar.number_input(min_value=18, max_value=110, label="Age")



    



if human_input and flag==True and thread_id and age>=18:
    with st.spinner("Thinking...!"):
            
        config = {"configurable" : {'thread_id':thread_id}}
        
        graph_tree=st.session_state['graph_tree']
        initial_state= {'messages': [HumanMessage(content= human_input)]}
        output = graph_tree.invoke(initial_state, config=config)
        response = output['messages'][-1].content


        with st.chat_message("user"):
            st.write(human_input)
        st.session_state['message_history'].append({'role': 'user', 'content': human_input})


        with st.chat_message("assistant"):
            st.write(response)
        st.session_state['message_history'].append({'role': 'assistant', 'content': response})

        st.rerun()
        # print(graph_tree)


        