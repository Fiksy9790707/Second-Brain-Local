from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import re
from typing import Any


@dataclass(frozen=True)
class Chunk:
    source: str
    index: int
    text: str
    score: int = 0


def load_markdown(path: Path, *, max_chars: int = 420) -> list[Chunk]:
    text = path.read_text(encoding="utf-8")
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[Chunk] = []

    for paragraph in paragraphs:
        for piece in _split_long_text(paragraph, max_chars=max_chars):
            chunks.append(Chunk(source=path.name, index=len(chunks), text=piece))

    return chunks


def retrieve(query: str, chunks: list[Chunk], *, top_k: int = 3) -> list[Chunk]:
    query_terms = _tokenize(query)
    scored: list[Chunk] = []

    for chunk in chunks:
        chunk_terms = _tokenize(chunk.text)
        score = len(query_terms & chunk_terms)
        if score:
            scored.append(Chunk(source=chunk.source, index=chunk.index, text=chunk.text, score=score))

    scored.sort(key=lambda item: (-item.score, item.index))
    return scored[:top_k]


def answer_query(query: str, matches: list[Chunk]) -> dict[str, Any]:
    if not matches:
        return {
            "query": query,
            "answer": "No matching local note chunks were found.",
            "contexts": [],
        }

    context_text = " ".join(match.text for match in matches)
    return {
        "query": query,
        "answer": _draft_answer(context_text),
        "contexts": [asdict(match) for match in matches],
    }


def _draft_answer(context: str) -> str:
    sentences = re.split(r"(?<=[.!?。！？])\s+", context.strip())
    useful = [sentence for sentence in sentences if sentence]
    return " ".join(useful[:2])


def _split_long_text(text: str, *, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    return [text[start : start + max_chars].strip() for start in range(0, len(text), max_chars)]


def _tokenize(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]{2,}", text)}
