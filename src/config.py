import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

def get_hf_token():
    hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not hf_token:
        raise EnvironmentError("HUGGINGFACE_API_TOKEN missing from .env file.")
    return hf_token

def get_hf_client(model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
                  token: str | None = None):
    if token is None:
        token = get_hf_token()

    return InferenceClient(model=model,
                           token=token
                           )