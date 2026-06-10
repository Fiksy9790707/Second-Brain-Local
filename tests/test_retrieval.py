from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from second_brain_local.retrieval import answer_query, load_markdown, retrieve


def test_retrieve_local_privacy_note():
    chunks = load_markdown(ROOT / "examples" / "sample_notes.md")
    matches = retrieve("local RAG privacy", chunks)
    assert matches
    assert matches[0].score > 0
    assert "Local RAG" in matches[0].text


def test_answer_query_shape():
    chunks = load_markdown(ROOT / "examples" / "sample_notes.md")
    matches = retrieve("Ollama ChromaDB", chunks)
    result = answer_query("Ollama ChromaDB", matches)
    assert result["query"] == "Ollama ChromaDB"
    assert isinstance(result["contexts"], list)
