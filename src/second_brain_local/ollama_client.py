from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

from .retrieval import Chunk


@dataclass(frozen=True)
class OllamaResult:
    used_ollama: bool
    answer: str
    fallback_reason: str | None = None


def build_prompt(query: str, contexts: list[Chunk]) -> str:
    context_text = "\n\n".join(f"[{item.source}#{item.index}] {item.text}" for item in contexts)
    return (
        "You are a local second-brain assistant. Answer only from the provided context. "
        "If the context is insufficient, say what is missing.\n\n"
        f"Question:\n{query}\n\n"
        f"Context:\n{context_text}\n"
    )


def generate_with_ollama(
    query: str,
    contexts: list[Chunk],
    *,
    model: str = "llama3.2:3b",
    endpoint: str = "http://127.0.0.1:11434/api/generate",
    timeout_seconds: float = 8.0,
) -> OllamaResult:
    prompt = build_prompt(query, contexts)
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    request = Request(endpoint, data=payload, headers={"Content-Type": "application/json"})

    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            data: dict[str, Any] = json.loads(response.read().decode("utf-8"))
    except (OSError, TimeoutError, URLError, json.JSONDecodeError) as exc:
        return OllamaResult(
            used_ollama=False,
            answer="Ollama is unavailable, so the demo kept the deterministic retrieval draft.",
            fallback_reason=type(exc).__name__,
        )

    answer = str(data.get("response") or "").strip()
    if not answer:
        return OllamaResult(
            used_ollama=False,
            answer="Ollama returned an empty response, so the demo kept the deterministic retrieval draft.",
            fallback_reason="empty_response",
        )

    return OllamaResult(used_ollama=True, answer=answer)
