import urllib.request
import json

req = urllib.request.Request('http://127.0.0.1:5000/api/generate', method='POST')
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        if data['success']:
            print(f"SUCCESS! Stats: {data['stats']}")
            print(f"First trace: {data['trace'][0]}")
            print(f"Last trace: {data['trace'][-1]}")
        else:
            print(f"FAILED. Stats: {data['stats']}")
            print(f"Last trace: {data['trace'][-1]}")
except Exception as e:
    print("Error connecting to server:", e)
