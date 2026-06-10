"""Small local retrieval helpers for Second-Brain-Local."""

from .ollama_client import OllamaResult, build_prompt, generate_with_ollama
from .retrieval import Chunk, answer_query, load_markdown, retrieve

__all__ = [
    "Chunk",
    "OllamaResult",
    "answer_query",
    "build_prompt",
    "generate_with_ollama",
    "load_markdown",
    "retrieve",
]
