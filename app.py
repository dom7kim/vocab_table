import streamlit as st
import requests
import warnings

# Filter out the specific warning
warnings.filterwarnings('ignore', 'The widget with key', category=UserWarning)

# Set the layout of the app to wide
st.set_page_config(layout="wide")

st.title('🦜️🔗Vocabulary Table Generator')
vocab_table_generator_url = "http://localhost:8000/create_vocab_table"

st.write('<p style="font-size:22px;">Let\'s make learning fun! This app crafts a unique vocabulary table just for you. It\'s filled with key expressions, their meanings in Korean and English, and contextually similar example sentences inspired by your original text. Enjoy your personalized language learning journey!</p>',
unsafe_allow_html=True)

st.write('<p style="font-size:22px;"> Please input text below, up to a maximum of 1000 characters.</p>',
unsafe_allow_html=True)

# Set default text
with open('Example.txt', 'r') as f:
    example_text = f.read()

# Set key for text_area widget
text_area = st.text_area("", value=example_text, key='text_area', height=200, max_chars=1000)

if st.button("Generate Table"):
        
    response = requests.post(vocab_table_generator_url,
                json={"original_text": text_area})
    #print(response.json()["table"])    
    output_table = response.json()["output_table"]
    #st.success(output_table)

    # Display HTML
    st.markdown(output_table, unsafe_allow_html=True)

# Define callback function to clear text
def clear_text():
    st.session_state["text_area"] = ""

# Set button with callback function
st.button("Clear Text", on_click=clear_text)