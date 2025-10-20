# manager

import os
import json
from typing import Any, List, Dict, Optional

SNIPPETS_DIR = "snippets"


def get_file_path(lang: str):
    """Return the JSON file path for the given language"""
    os.makedirs(SNIPPETS_DIR, exist_ok=True)
    return os.path.join(SNIPPETS_DIR, f"{lang.lower()}.json")


def _read_json(file_path: str) -> List[Dict[str, Any]]:
    """Read JSON data safely, returning an empty list if missing or invaild."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"Warning: {file_path} was invaild or empty. Resettings file.")
        return []


def _write_json(file_path: str, data: List[Dict[str, Any]]) -> None:
    """Write JSON data safely"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add(snippets: Dict[str, Any]) -> bool:
    """Add a new snippets to the JSON file for the given language"""
    lang = snippets.get("language")
    if not lang:
        print("Error: snippets missing'language' key.")
        return False

    file_path = get_file_path(lang)
    data = _read_json(file_path)
    data.append(snippets)
    _write_json(file_path, data)

    print(f"✅ Added snippet: {snippets.get('title', 'Untitled')} to {lang}")
    return True


def delete(title: str, lang: str) -> bool:
    """Delete a snippet by title."""
    file_path = get_file_path(lang)
    data = _read_json(file_path)

    new_data = [s for s in data if s.get("title") != title]
    if len(new_data) == len(data):
        print(f"⚠️ No snippet found with title '{title}'.")
        return False
    _write_json(file_path, new_data)
    print(f"🗑️ Deleted snippet '{title}' from {lang}.")
    return True


def search(term: str, lang: str) -> Optional[List[Dict[str, Any]]]:
    """Search for snippets containing the term in their title and print them."""
    file_path = get_file_path(lang)
    data = _read_json(file_path)
    results = [
        s
        for s in data
        if isinstance(s, dict) and term.lower() in s.get("title", "").lower()
    ]

    if not results:
        print(f"No matches found for '{term}':")
        print(json.dumps(results, indent=4))

    print(f"\nFound {len(results)} match(es) for '{term}':\n")
    for snippets in results:
        title = snippets.get("title", "Untitled")
        code = snippets.get("code", "[No code available]")
        print(f"📘 Title: {title}")
        print("─" * 60)
        print(code)
        print("─" * 60 + "\n")

    return results


def view_snippets(lang: str) -> Optional[List[Dict[str, Any]]]:
    """View all snippets for a given language"""
    file_path = get_file_path(lang)
    data = _read_json(file_path)
    if not data:
        print(f"No snippets found for {lang}.")
        return None

    print(f"📚 All snippets for {lang}:")
    print(json.dumps(data, indent=4))
    return data


def view_options() -> None:
    # user Options viewer
    print("Options available are: ")
    print("1. Add a snippet")
    print("2. Delete a snippet")
    print("3. Search snippets")
    print("4. View all snippets")
