from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from second_brain_local.ollama_client import generate_with_ollama
from second_brain_local.retrieval import answer_query, load_markdown, retrieve


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a minimal local note retrieval demo.")
    parser.add_argument("--query", default="What does the note say about local RAG privacy?")
    parser.add_argument("--notes", type=Path, default=ROOT / "examples" / "sample_notes.md")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--use-ollama", action="store_true", help="Try local Ollama generation.")
    parser.add_argument("--ollama-model", default="llama3.2:3b")
    args = parser.parse_args()

    chunks = load_markdown(args.notes)
    matches = retrieve(args.query, chunks, top_k=args.top_k)
    result = answer_query(args.query, matches)

    if args.use_ollama and matches:
        ollama_result = generate_with_ollama(args.query, matches, model=args.ollama_model)
        result["ollama"] = {
            "requested": True,
            "used": ollama_result.used_ollama,
            "fallback_reason": ollama_result.fallback_reason,
        }
        if ollama_result.used_ollama:
            result["answer"] = ollama_result.answer
        else:
            result["ollama"]["fallback_message"] = ollama_result.answer
    else:
        result["ollama"] = {"requested": False, "used": False, "fallback_reason": None}

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
