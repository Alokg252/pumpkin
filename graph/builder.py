import os
import json
import re

from llm import ask_llm
from graph.graph import GraphDB


def extract_json(text):

    print('<------------------ start ---------------->',text,'<------------------- end ----------------->')

    match = re.search(r"\[.*\]", text, re.S)

    if not match:
        raise ValueError("No JSON found in LLM output")

    return match.group()


def extract_relations(text):

    prompt = f"""
Extract entities and relations from this text.

Return ONLY valid JSON array.

Format:

[
  {{
    "head": "Entity1",
    "relation": "relation",
    "tail": "Entity2"
  }}
]

Text:
{text}
"""

    res = ask_llm(prompt)

    json_text = extract_json(res)

    return json.loads(json_text)


def build_graph_from_text(text):

    db = GraphDB()

    triples = extract_relations(text)

    for t in triples:

        db.add_relation(
            t["head"],
            t["relation"],
            t["tail"]
        )

    db.close()
