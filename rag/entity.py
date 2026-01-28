from llm import ask_llm


def extract_entity(query):

    prompt = f"""
Extract main technical entity from this question.

Return only the entity name.

Question:
{query}
"""

    res = ask_llm(prompt)

    return res.strip()
