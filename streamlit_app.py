# Adityas.com
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

st.set_page_config(page_title="AdChat", layout="centered")

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# For Streamlit Cloud deployment
if not GROQ_API_KEY:
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except FileNotFoundError:
        pass
    except KeyError:
        pass

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY is missing. Please add it to your .env file or Streamlit secrets.")
    st.stop()


@st.cache_resource
def load_llm():
    return ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7,
        groq_api_key=GROQ_API_KEY
    )

llm = load_llm()


st.title("AdChats")

user_input = st.text_area("ask anything 👇", height=150)

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter a prompt!")
    else:
        try:
            st.subheader("🤖 Response:")
            response_placeholder = st.empty()
            full_response = ""

            for chunk in llm.stream(user_input):
                if chunk.content:
                    full_response += chunk.content
                    response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"❌ Error: {e}")
