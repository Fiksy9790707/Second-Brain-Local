# Local RAG Notes

Local RAG keeps personal notes on the user's own machine. This is useful when the notes contain private study plans, project ideas, or personal records.

The workflow usually has four steps: load documents, split them into chunks, retrieve relevant chunks, and send the selected context to a language model.

This project starts with a keyword retrieval baseline before adding embeddings or a vector database. A simple baseline makes it easier to test data flow and output format.

Ollama can later be used as a local LLM runtime. ChromaDB can later provide persistent vector storage for retrieved chunks.
