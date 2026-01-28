from search.retriever import search
from llm import ask_llm
from rag.entity import extract_entity
from graph.search import GraphSearch


def rag(query):

    # 1. Vector retrieval
    docs = search(query)

    # 2. Entity extraction
    entity = extract_entity(query)

    # 3. Graph expansion
    gs = GraphSearch()
    relations = gs.get_neighbors(entity)
    gs.close()

    graph_context = "\n".join(relations)

    vector_context = "\n".join(d["text"][:1500] for d in docs)

    # 4. Final prompt
    prompt = f"""
Answer using the following knowledge.

Graph Relations:
{graph_context}

Relevant Notes:
{vector_context}

Question:
{query}
"""

    return ask_llm(prompt)
