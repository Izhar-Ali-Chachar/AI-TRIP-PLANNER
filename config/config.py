from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class Call_LLM:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
