# tagger.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access the environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

class Classification(BaseModel):
    sentiment: str = Field(description="The sentiment of the text")
    aggressiveness: int = Field(description="How aggressive the text is on a scale from 1 to 10")
    language: str = Field(description="The language the text is written in")

tagging_prompt = ChatPromptTemplate.from_template(
    """
Extract the desired information from the following passage.

Only extract the properties mentioned in the 'Classification' function.

Passage:
{input}
"""
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
).with_structured_output(
    Classification
)

tagging_chain = tagging_prompt | llm

def tag_article(article_text):
    """Tag the article text and return classification results."""
    try:
        res = tagging_chain.invoke({"input": article_text})
        return res.dict()
    except Exception as e:
        print(f"Error during tagging: {e}")
        return {'sentiment': 'Not Available', 'aggressiveness': 'Not Available', 'language': 'Not Available'}

