import os
import requests
import json


def visualize_query(description: str, title: str) -> requests.Response:
    __HF_API_TOKEN = os.getenv("HF_API_TOKEN")
    __MODEL_NAME = "DGSpitzer/Cyberpunk-Anime-Diffusion"
    __API_URL = f"https://api-inference.huggingface.co/models/{__MODEL_NAME}"
    headers = {"Authorization": f"Bearer {__HF_API_TOKEN}"}
    text = f"{description} in {title} world"
    data = json.dumps(text)
    return requests.request("POST", __API_URL, headers=headers, data=data)
