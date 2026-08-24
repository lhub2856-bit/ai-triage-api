# ai-triage-api
This is API triage api assignment
# AI Support Triage API

A professional, production-ready FastAPI application that integrates an LLM (via OpenAI/OpenRouter) to automatically categorize incoming customer support messages, assess urgency, and provide confidence scores with a structured reasoning.

## 🚀 Features
- **FastAPI Backend**: High-performance, asynchronous API framework.
- **Pydantic Validation**: Strict input and output schema validation (`SupportInput` & `SupportOutput`).
- **Versioned Prompt Management**: Separated prompt templates stored in the `prompts/` directory (`triage-v1.md`).
- **Stub Mode**: Built-in testing mode (`LLM_STUB=1`) to test endpoints without consuming LLM credits.
- **Secure Configuration**: Uses environment variables (`.env`) to prevent hardcoded API keys.

---

## 📂 Project Structure
```text
ai-triage-api/
│
├── main.py              # FastAPI application and endpoint logic
├── prompts/
│   └── triage-v1.md     # Versioned system prompt
├── JOB-CARD.md          # Project blueprint and requirements
├── .gitignore           # Excludes .env and cache files
└── README.md            # Project documentation
