import requests
endpoint = 'https://api.together.xyz/v1/chat/completions'

def getplaintext(prompt, maxlength):
    res = requests.post(endpoint, json={
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "max_tokens": maxlength,
        "prompt": f"[INST] {prompt} [/INST]",
        "request_type": "language-model-inference",
        "temperature": 0.1,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": [
            "[/INST]",
            "</s>"
        ],
        "promptObj": {
            "prompt": prompt
        }
    }, headers={
        "Authorization": "Bearer f7e58960014e29d3c334f16508842b8d4ec53debc023f3579812dd9a62ab49e1",
    })
    return res.json()['choices'][0]['message']['content']




