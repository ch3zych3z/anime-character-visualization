import os
import requests
import json


def get_text(description: str, title: str) -> str:
    return f"{description} in {title} world"


def visualize_query(description: str, title: str) -> requests.Response:
    hf_api_token = os.getenv("HF_API_TOKEN")
    model_name = "DGSpitzer/Cyberpunk-Anime-Diffusion"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {hf_api_token}"}
    text = get_text(description, title)
    data = json.dumps(text)
    return requests.request("POST", api_url, headers=headers, data=data)
