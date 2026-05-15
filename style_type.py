

import streamlit as st 


def set_page_config():

    x=st.set_page_config(
        page_title="Pharma ChatBot", page_icon="⚕️",
        initial_sidebar_state="expanded", #["auto", 'collasped', 'expanded]
        layout='wide' 
    )
    return x

def sidebarStyle():
    x=st.markdown(""" <style>
                [data-testid='stSidebar']  {background-color: #330000}
                [data-testid='stSidebar'] * {color: #FFFF00}
                [data-testid='stSidebar'] input {background-color: #330000 !important;
                        color: #FFFF00 !important;}
                [data-testid='stSidebar'] [data-testid='stSelectbox'] * {
                        background-color: #330000 !important;
                        color: #FFFF00 !important;
                    }
                [data-testid='stSidebar'] [data-testid='stTextInput'] button svg {
                                                                                    fill: #001933}
                                /* Label color */
                    [data-testid='stSidebar'] [data-testid='stSelectbox'] label {
                        color: #001933;
                    }

                    /* Selected value color */
                    [data-testid='stSidebar'] [data-testid='stSelectbox'] span {
                        color: #001933;
                                    }
                                
                                /* Selectbox background aur text */
                [data-testid='stSidebar'] [data-testid='stSelectbox'] div[data-baseweb='select'] {
                    background-color: #330000;
                    color: #000000;
                }

                /* Dropdown selected value */
                [data-testid='stSidebar'] [data-testid='stSelectbox'] div[data-baseweb='select'] span {
                    color: #000000;
                }

                /* Selectbox container */
                [data-testid='stSidebar'] [data-testid='stSelectbox'] div[role='combobox'] {
                    background-color: #330000;
                    color: #000000;
                }
                                
                                
                                .stApp {background-color : #ccffcc; color: #1a1a2e;}

                                h1 { color: #80ff00;}
                                </style>   """, unsafe_allow_html=True)
    return x
            
                
                
                

                
                
                




def mainpageStyle():
    x=st.markdown("""<style>
                [data-testid="stChatInput] textarea {background-color: #1e1e2f;
            color: #ffffff;}
                
                /* Chat input border */
            [data-testid='stChatInputContainer'] {
                background-color: #1e1e2f;
                border: 1px solid #4ecdc4;
                
                /* Send button */
                [data-testid='stChatInputSubmitButton'] svg {
            fill: #ffffff;
                </style>
                """, unsafe_allow_html=True)
    return x


def chatInputStyle():
    

    x= st.markdown("""
                <style>
                /* Chat input box background aur text color */
                [data-testid='stChatInput'] textarea {
                    background-color: #FFFF00;
                    color: #330000;
                }
                
                /* Chat input border */
                [data-testid='stChatInputContainer'] {
                    background-color: #4ecdc4;
                    border: 1px solid #4ecdc4;
                }
                
                /* Send button */
                [data-testid='stChatInputSubmitButton'] svg {
                    fill: #4ecdc4;
                }
                   


                   
                </style>
            """, unsafe_allow_html=True)
    return x



def userAIStyle():
    x= st.markdown("""
                <style>
                /* User message background */
                [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
                    background-color: #1a1a2e;
                    border-radius: 10px;
                    padding: 10px;
                    color: #00ff99;
                }
                
                /* Assistant message background */
                [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
                    background-color: #2d0033;
                    border-radius: 30px;
                    padding: 10px;
                    color: #ffcc00;
                }
                </style>
            """, unsafe_allow_html=True)
    return x

def newStyle():
    st.markdown("""
        <style>
        [data-testid='stSidebar'] [data-testid='stSelectbox'] div[data-baseweb='select'] {
            background-color: #2d0033;
            color: #000000 !important;
        }

        [data-testid='stSidebar'] [data-testid='stSelectbox'] div[data-baseweb='select'] span {
            color: #000000 !important;
        }

        [data-testid='stSidebar'] [data-testid='stSelectbox'] div[role='combobox'] {
            background-color: #2d0033;
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)