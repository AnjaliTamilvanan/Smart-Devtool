def generate_code(data, language):

    if language == "python":
        return """
import requests

def call_api():
    url = "YOUR_ENDPOINT"
    response = requests.get(url)
    return response.json()
"""

    if language == "javascript":
        return """
fetch("YOUR_ENDPOINT")
  .then(res => res.json())
  .then(data => console.log(data));
"""