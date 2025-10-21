# cli
# cli/system.py
from .manager import view_options
from .utils import get_confirmation, get_int_input, handle_choices
from .logo import ascii_logo


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
