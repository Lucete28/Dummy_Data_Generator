import streamlit as st
from Main import *
import time
def page_set():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "hello"
    if st.session_state["current_page"] == "hello":
        hello()
        
    elif st.session_state["current_page"] == "main":
        main()
    
def hello():
    st.write("Hello World")
    if st.button("이용하기"):
        page_change("main")

        
def page_change(page,message=None):
    if message:
        st.session_state["alert_message"] = message
    st.session_state["current_page"]= f"{page}"
    st.experimental_rerun()   
        
if __name__ == "__main__":
    page_set()
    # st.experimental_rerun()