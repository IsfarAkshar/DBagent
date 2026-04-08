from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("LLM_MODEL_PATH")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, trust_remote_code=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)  # CPU

def generate_sql(prompt: str, max_tokens: int = 200) -> str:
    output = generator(prompt, max_new_tokens=max_tokens, do_sample=False)
    return output[0]['generated_text']