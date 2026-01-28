from neo4j import GraphDatabase
import os


class GraphDB:

    def __init__(self):

        self.uri = os.getenv("NEO4J_URI")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASS")

        self.driver = GraphDatabase.driver(
            self.uri,
            auth=(self.user, self.password)
        )


    def close(self):
        self.driver.close()


    def add_relation(self, head, relation, tail):

        query = """
        MERGE (h:Entity {name: $head})
        MERGE (t:Entity {name: $tail})
        MERGE (h)-[r:REL {type: $rel}]->(t)
        """

        with self.driver.session() as session:
            session.run(
                query,
                head=head,
                tail=tail,
                rel=relation
            )


    def clear(self):

        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
