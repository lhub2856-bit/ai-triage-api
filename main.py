import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from openai import OpenAI

app = FastAPI()

# OpenAI client initialization using environment variables
client = OpenAI(
    base_url=os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.environ.get("LLM_API_KEY", "dummy-key")
)

# Input Schema
class SupportInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)

# Output Schema
class SupportOutput(BaseModel):
    category: Literal["billing", "bug", "feature", "other"]
    urgency: Literal["low", "normal", "high"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    reason: str

# Helper to load versioned prompt
def load_prompt():
    prompt_path = os.path.join("prompts", "triage-v1.md")
    if os.path.exists(prompt_path):
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    return "You are a helpful support classifier. Return valid JSON only."

@app.post("/triage", response_model=SupportOutput)
def triage_message(payload: SupportInput):
    # 1. Stub Mode check (Testing ke liye bina AI ke chalana)
    if os.environ.get("LLM_STUB") == "1":
        return {
            "category": "bug",
            "urgency": "normal",
            "confidence": 0.95,
            "reason": "Stub mode active response for testing."
        }
    
    # 2. Real LLM Call
    system_prompt = load_prompt()
    
    try:
        response = client.chat.completions.create(
            model=os.environ.get("LLM_MODEL", "openrouter/free"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": payload.text}
            ],
            response_format={"type": "json_object"} # Ensure JSON output from model
        )
        
        content = response.choices[0].message.content
        result_data = json.loads(content)
        return result_data
        
    except Exception as e:
        # Agar AI ya JSON parsing mein koi masla ho toh 422 error return karega
        raise HTTPException(status_code=422, detail=f"LLM processing failed: {str(e)}")