from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from parser import load_all
from embedder import embed


client = QdrantClient("localhost", port=6333)


COLLECTION = "pkis"


def setup():

    client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config={
            "size": 384,
            "distance": "Cosine"
        }
    )


def ingest():

    docs = load_all()

    points = []

    for i, doc in enumerate(docs):

        vec = embed(doc["text"][:2000])

        payload = {
            "path": doc["path"],
            "text": doc["text"]
        }

        points.append(
            PointStruct(
                id=i,
                vector=vec,
                payload=payload
            )
        )

    client.upsert(COLLECTION, points)

    print("Indexed:", len(points))


if __name__ == "__main__":

    setup()
    ingest()
