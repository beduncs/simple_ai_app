# Simple Serving

This is a simple LLM serving example using Llama.cpp, FastAPI and Pydantic.

## Quick Start

### Pre-requisites

This application requires a local OpenAI API services running at `http://localhost:8000`.

```bash

### Local

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-1234
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

### Docker

```bash
docker build -t simple_ai_app .
docker run -p 8080:8080 -e OPENAI_API_KEY=sk-1234 simple_ai_app
```