import streamlit as st
import requests

st.title('🦜️🔗Vocabulary Table Generator')
vocab_table_generator_url = "http://localhost:8000/create_vocab_table"

text = st.text_input("text")

if st.button("Generate Table"):
        
    response = requests.post(vocab_table_generator_url,
                json={"original_text": text})
    #print(response.json()["table"])    
    output_table = response.json()["output_table"]
    st.success(output_table)
