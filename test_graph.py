from graph.builder import build_graph_from_text


text = """
Hibernate uses SessionFactory to create sessions.
Session manages database connections.
Hibernate is an ORM framework.
"""

build_graph_from_text(text)

print("Done")
