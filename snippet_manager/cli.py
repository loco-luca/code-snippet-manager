# cli
# cli/system.py
from typing import Optional
from .manager import delete, add, search, view_options, view_snippets
from .utils import generate_snippet_data
from .logo import ascii_logo


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


def system():
    ascii_logo()
    print("\n")
    supported_languages = ["Python", "Rust", "Dart"]

    while True:
        print(f"Currently supported languages -> {supported_languages}")
        user_input = input("Select a language or 'q' to quit: ").strip().lower()

        if not user_input:
            print("Please enter your choice.")
            continue

        if user_input == "q":
            if get_confirmation("Are you sure you want to quit? "):
                print("Closing Code Snippet Manager.")
                break
            else:
                print("Back to main menu.")
                continue

        if user_input.capitalize() not in supported_languages:
            print("Language not supported yet.")
            continue

        if not get_confirmation(f"Proceed with {user_input.capitalize()}?"):
            print("Cancelled.")
            continue

        view_options()
        user_choice = get_int_input("Enter a number matching your choice: ")
        if user_choice is None:
            continue

        handle_choices(user_choice, user_input)
