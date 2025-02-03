import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from transformers import MarianMTModel, MarianTokenizer

app = FastAPI()

# For demonstration, let's assume we want English -> Spanish
model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = MarianTokenizer.from_pretrained(model_name)
translation_model = MarianMTModel.from_pretrained(model_name)

# This class defines the request body
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
def translate_text(request: TranslationRequest):
    # Check for token in environment or request headers for "Groq API"
    api_token = os.environ.get("GROQ_API_TOKEN", None)
    # if needed, we can also check request.headers.get("Authorization")
    if api_token is None:
        return {"error": "No Groq API token provided"}

    # Perform translation
    inputs = tokenizer(request.text, return_tensors="pt", truncation=True)
    outputs = translation_model.generate(**inputs, max_new_tokens=40)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"translated_text": translated_text}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
