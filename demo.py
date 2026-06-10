from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from second_brain_local.retrieval import answer_query, load_markdown, retrieve


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a minimal local note retrieval demo.")
    parser.add_argument("--query", default="What does the note say about local RAG privacy?")
    parser.add_argument("--notes", type=Path, default=ROOT / "examples" / "sample_notes.md")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    chunks = load_markdown(args.notes)
    matches = retrieve(args.query, chunks, top_k=args.top_k)
    result = answer_query(args.query, matches)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
