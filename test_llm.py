from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv() 

llm = GoogleGenerativeAI(
    model="gemini-2.5-pro"
)
res = llm.invoke('Hello my name is Aditya. What is your name?')

print(res)