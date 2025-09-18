import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding_safe(text: str, model: str = "text-embedding-3-small"):
    """
    Returns a dummy embedding if OpenAI API is not available.
    """
    if not openai.api_key:
        # Return a zero vector of length 1536 for testing
        return [0.0] * 1536
    try:
        response = openai.Embedding.create(input=text, model=model)
        return response["data"][0]["embedding"]
    except Exception:
        # fallback zero vector on error
        return [0.0] * 1536


def get_embedding(text: str):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]

def ask_openai(question: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]
