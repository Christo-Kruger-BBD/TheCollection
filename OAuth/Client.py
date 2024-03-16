import requests
from typing import List, Dict

class Client:
    def postLogin(self, login: dict, headers: Dict[str, str]) -> str:
        url = "https://github.com/login/device/code"
        response = requests.post(url, json=login, headers=headers)
        return response.text

    def postAuth(self, authResponse: dict, headers: Dict[str, str]) -> str:
        url = "https://github.com/login/oauth/access_token"
        response = requests.post(url, json=authResponse, headers=headers)
        return response.text

    def getUserId(self, headers: Dict[str, str]) -> int:
        url = "https://example.com/getUserID"  # Replace example.com with your actual endpoint
        response = requests.get(url, headers=headers)
        return response.json()["userId"]  # Assuming the response contains JSON with a key "userId"
