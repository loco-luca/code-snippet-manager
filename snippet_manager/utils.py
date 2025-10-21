from .storage import CodeSnippets
from dataclasses import asdict
import uuid
import shutil
from .manager import *


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


def get_confirmation(prompt: str) -> bool:
    """Ask for yes/no confirmation."""
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice == "y"


def get_int_input(prompt: str) -> Optional[int]:
    """Get integer input safely, returning None if invalid."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number. Please try again.")
        return None


def handle_choices(choice: int, language: str):
    """Handle the snippet manager options."""
    if choice == 1:
        code_snippet = generate_snippet_data(language)
        add(code_snippet)
    elif choice == 2:
        title = input("Please enter title: ").strip()
        delete(title, language)
    elif choice == 3:
        term = input("Search: ").strip()
        search(term, language)
    elif choice == 4:
        view_snippets(language)
    else:
        print("Invalid option selected.")
