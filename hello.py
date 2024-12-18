from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM with your Google API key
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("MASSAB_GOOGLE_API")
)

# Define the review to analyze
review = """asalam mu alikum ... intehai ghatiya airpods ha koi order na kre 4 din charge hue chalay ab sara din b charge pr lage rhe
tb b ni chalte paisa waste hue mere kachara airpods ... 
"""

# Define the prompt for the LLM
prompt = f"""Become a product reviewer, analyze the product review 
and summarize it in 20 words. Also, give the sentiment of the review using only 
these words given in square brackets [Positive, Negative, Neutral]. Define 3 main highlights in the review.

Format the response in JSON in the following way:
1. Product
2. Review Summary
3. Sentiment
4. Highlights

The review is given in triple backticks:
```{review}```
"""

# Invoke the LLM with the prompt
response = llm.invoke([prompt])

# Print the response
print(response)
