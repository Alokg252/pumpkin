from qdrant_client import QdrantClient
from ingest.embedder import embed


client = QdrantClient("localhost", port=6333)

COLLECTION = "pkis"


def search(query, k=5):

    vec = embed(query)

    res = client.query_points(
        collection_name=COLLECTION,
        query=vec,
        limit=k
    )

    return [p.payload for p in res.points]
