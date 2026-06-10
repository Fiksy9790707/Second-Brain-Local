# Second-Brain-Local

A work-in-progress local knowledge-base and retrieval workflow experiment.

This repository explores a small, privacy-friendly "second brain" workflow: load local notes, split them into searchable chunks, retrieve relevant context for a query, and prepare a response structure that can later be connected to Ollama or another local LLM runtime.

The current version is intentionally modest. It is not a finished RAG product and does not claim production-level retrieval quality.

## Current Status

- Minimal local retrieval demo: implemented
- Markdown note loading and chunking: implemented
- Simple keyword scoring baseline: implemented
- Ollama answer generation: planned
- ChromaDB vector storage: planned
- Streamlit interface: planned

## Why This Project

Personal notes often contain useful but scattered information. This project tests a local-first workflow for retrieving relevant note fragments without uploading private materials to cloud services.

## Minimal Demo

Run the current local demo:

```bash
python demo.py --query "What does the note say about local RAG privacy?"
```

The demo prints JSON with:

- the original query
- a draft answer based on retrieved context
- the top matching note chunks

## Project Structure

```text
Second-Brain-Local/
├── README.md
├── demo.py
├── examples/
│   ├── sample_notes.md
│   └── sample_query.json
├── src/
│   └── second_brain_local/
│       ├── __init__.py
│       └── retrieval.py
└── tests/
    └── test_retrieval.py
```

## Technical Direction

- `Python` for local workflow implementation
- `Ollama` for future local LLM generation
- `RAG` workflow design: load, chunk, retrieve, assemble context, generate answer
- `ChromaDB` planned for persistent vector storage
- `Streamlit` planned for a lightweight local interface

## Current Limitations

- Retrieval currently uses a simple keyword overlap baseline, not embeddings.
- No private notes should be committed to the repository.
- LLM generation is not wired yet; current output is a deterministic draft based on retrieved context.
- ChromaDB and Ollama are planned next steps, not current hard dependencies.

## Roadmap

1. Add a document loader for local Markdown folders.
2. Replace keyword scoring with embeddings.
3. Add optional ChromaDB persistence.
4. Add Ollama-based answer generation with a fallback when Ollama is unavailable.
5. Add a small Streamlit interface for local testing.

## Notes

This project is kept realistic and work-in-progress. It is mainly evidence of learning and building a local RAG workflow step by step.
