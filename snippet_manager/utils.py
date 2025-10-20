from .storage import CodeSnippets
from dataclasses import asdict
from .manager import get_file_path
import uuid
import shutil


def format_snippets_data(title: str, language: str, code: str) -> dict:
    """Convert snippet details into a dictionary suitable for JSON storage."""
    snippet = CodeSnippets(
        id=str(uuid.uuid4()),
        title=title.strip(),
        language=language.strip(),
        code=code.strip(),
    )
    return asdict(snippet)


def generate_snippet_data(lang: str) -> dict:
    """Prompt the user for snippet details and return formatted snippet data."""
    title = input("Enter snippet title: ").strip()
    code = input("Enter code snippet: ").strip()
    return format_snippets_data(title, lang, code)


def print_centered(text: str) -> None:
    """Print text centered based on terminal width."""
    try:
        width = shutil.get_terminal_size().columns
    except OSError:
        width = 80

    for line in text.splitlines():
        print(line.center(width))
