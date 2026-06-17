import requests 

url = "https://raw.githubusercontent.com/RishitUmeshPadagatti/GenAI/refs/heads/main/6.py"
code = requests.get(url).text

print(code)