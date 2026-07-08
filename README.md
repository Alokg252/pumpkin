# Pumpkin

Pumpkin is a small Python project that turns local notes and code into a searchable knowledge base and answers questions through a hybrid retrieval pipeline.

It combines:
- vector search over ingested text using Qdrant
- graph-based relation expansion using Neo4j
- LLM-generated answers using OpenAI, Gemini, or Ollama

## What this project does

The workflow is:
1. Read documents from the data folder
2. Convert them into embeddings
3. Store the embeddings in Qdrant
4. Extract entities and relationships from text with an LLM
5. Store those relationships in Neo4j
6. Answer a question by combining vector retrieval and graph context

## Project structure

- main.py: simple entry point for the sample RAG query
- llm.py: wrapper around the configured LLM backend
- config/settings.py: environment-based configuration
- ingest/: ingestion pipeline for parsing and embedding documents
- graph/: graph construction and graph-based search helpers
- rag/: entity extraction and answer composition
- search/: vector retrieval layer
- data/notes: markdown notes to ingest
- data/code: code files to ingest (if present)

## Prerequisites

You will need:
- Python 3.9+
- Qdrant running locally on port 6333
- Neo4j running locally
- An LLM backend configured through environment variables

## Installation

Install the required Python packages:

```bash
pip install requests openai python-dotenv sentence-transformers qdrant-client neo4j
```

## Configuration

Create a .env file in the project root with values similar to:

```env
LLM_MODE=ollama
OLLAMA_URL=http://localhost:11434
MODEL_NAME=llama3

OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key

NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASS=your-password
```

## Running the project

### 1. Ingest the documents

```bash
python ingest/ingest.py
```

This will:
- load markdown files from data/notes and code files from data/code
- create or recreate the Qdrant collection
- embed each document and store it in Qdrant

### 2. Run the sample query

```bash
python main.py
```

This runs a sample prompt through the RAG pipeline.

### 3. Build a sample graph

```bash
test_graph.py
```

This script creates a small graph from hard-coded example text using the graph builder.

## Notes

- The project is intentionally lightweight and demo-oriented.
- The vector layer is built around the sentence-transformers model all-MiniLM-L6-v2.
- The graph layer relies on Neo4j relationships extracted from LLM output.
- The code expects to be run from the project root.

## Future improvements

Possible enhancements include:
- adding a proper requirements.txt file
- adding a CLI interface for queries and ingestion
- improving error handling for missing services
- supporting more document formats
