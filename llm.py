import requests
import openai

from config.settings import *


def ask_llm(prompt):

    print("LLM Prompt:", prompt)

    if LLM_MODE == "openai":

        openai.api_key = OPENAI_KEY

        r = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}]
        )

        return r.choices[0].message.content

    elif LLM_MODE == "gemini":

        openai.api_key = GEMINI_KEY

        r = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}]
        )

        return r.choices[0].message.content


    else:

        res = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False   # 🔥 THIS
            }
        )

        data = res.json()

        return data["response"]
