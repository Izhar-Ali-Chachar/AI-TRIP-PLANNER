from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class Call_LLM:
    def __init__(self):
        self.llm = ChatGroq(model='llama3-70b-8192')
