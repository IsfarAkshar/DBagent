#import google.generativeai as genai
#import os

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#model = genai.GenerativeModel("gemini-1.0-pro")

#def generate_sql(prompt: str) -> str:
    #response = model.generate_content(prompt)
#    response = genai.generate_content(
#        model="models/gemini-1.5-flash",
#        contents=prompt
#    )
#    return response.text.strip()

###Gemini
#import google.generativeai as genai
#import os

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Compatible model for your SDK
#model = genai.GenerativeModel("models/text-bison-001")

#def generate_sql(prompt: str) -> str:
#    response = model.generate_content(prompt)
#    return response.text.strip()


##Openai
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def generate_sql(prompt: str) -> str:
    response = client.chat.completions.create(
        model="openrouter/auto",  # ✅ free models auto-selected
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
