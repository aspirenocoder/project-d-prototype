import streamlit as st
from helper.openai import response

st.title("AuralApp")

with st.form("user_inputs"):
    options = [ "ISL English to Standard English"]
    selected_option = st.selectbox("Select an option:", options)
    # st.write(f"You selected: {selected_option}"
    text = st.text_input("Enter text")

    button = st.form_submit_button("Submit")

    if button and text:
        try:
            # Call the response function from helper.openai
            resp = response(text, selected_option)
            st.write(resp.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
