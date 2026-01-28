from neo4j import GraphDatabase
import os


class GraphSearch:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USER"),
                os.getenv("NEO4J_PASS")
            )
        )


    def close(self):
        self.driver.close()


    def get_neighbors(self, entity, depth=2):

        query = f"""
        MATCH (n:Entity {{name: $name}})-[r*1..{depth}]-(m)
        RETURN DISTINCT n, r, m
        """

        with self.driver.session() as session:

            result = session.run(query, name=entity)

            facts = []

            for row in result:

                n = row["n"]["name"]
                m = row["m"]["name"]

                for rel in row["r"]:
                    facts.append(
                        f"{n} -> {rel['type']} -> {m}"
                    )

            return list(set(facts))
