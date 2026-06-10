# Second-Brain-Local

A work-in-progress local knowledge-base and retrieval workflow experiment.

This repository explores a small, privacy-friendly "second brain" workflow: load local notes, split them into searchable chunks, retrieve relevant context for a query, and prepare a response structure that can optionally be connected to a local Ollama runtime.

The current version is intentionally modest. It is not a finished RAG product and does not claim production-level retrieval quality.

## Current Status

- Minimal local retrieval demo: implemented
- Markdown note loading and chunking: implemented
- Simple keyword scoring baseline: implemented
- Optional Ollama generation adapter: implemented with fallback
- ChromaDB vector storage: planned
- Streamlit interface: planned

## Why This Project

Personal notes often contain useful but scattered information. This project tests a local-first workflow for retrieving relevant note fragments without uploading private materials to cloud services.

## Minimal Demo

Run the current local demo:

```bash
python demo.py --query "What does the note say about local RAG privacy?"
```

Try optional local Ollama generation:

```bash
python demo.py --query "What does the note say about local RAG privacy?" --use-ollama --ollama-model llama3.2:3b
```

If Ollama is not running, the demo falls back to the deterministic retrieval draft and records the fallback reason in the JSON output.

The demo prints JSON with:

- the original query
- a draft answer based on retrieved context
- the top matching note chunks
- Ollama usage metadata when `--use-ollama` is enabled

## Project Structure

```text
Second-Brain-Local/
|-- README.md
|-- demo.py
|-- examples/
|   |-- sample_notes.md
|   `-- sample_query.json
|-- src/
|   `-- second_brain_local/
|       |-- __init__.py
|       |-- ollama_client.py
|       `-- retrieval.py
`-- tests/
    `-- test_retrieval.py
```

## Technical Direction

- `Python` for local workflow implementation
- `Ollama` optional local LLM generation adapter
- `RAG` workflow design: load, chunk, retrieve, assemble context, generate answer
- `ChromaDB` planned for persistent vector storage
- `Streamlit` planned for a lightweight local interface

## Current Limitations

- Retrieval currently uses a simple keyword overlap baseline, not embeddings.
- No private notes should be committed to the repository.
- LLM generation is optional and depends on a local Ollama service.
- If Ollama is unavailable, the demo keeps a deterministic draft answer and records the fallback reason.
- ChromaDB is planned as a next step, not a current hard dependency.

## Roadmap

1. Add a document loader for local Markdown folders.
2. Replace keyword scoring with embeddings.
3. Add optional ChromaDB persistence.
4. Improve prompt templates and local generation settings.
5. Add a small Streamlit interface for local testing.

## Notes

This project is kept realistic and work-in-progress. It is mainly evidence of learning and building a local RAG workflow step by step.
