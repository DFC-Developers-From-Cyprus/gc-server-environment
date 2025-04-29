import os
import requests

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


def test(location):
    test_link = f"https://api.waqi.info/feed/{location}/?token={TOKEN}"
    return requests.get(test_link).content
